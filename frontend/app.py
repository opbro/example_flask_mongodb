from flask import Flask, request, url_for, jsonify
from pymongo import MongoClient
from uuid import uuid4

# TODO:  Will need to replace with actual AD at some point
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

import os

CERT_PEM_PATH = os.getenv('CERT_PEM_PATH', 'cert.pem')
KEY_PEM_PATH = os.getenv('KEY_PEM_PATH', 'key.pem')

app = Flask(__name__)
auth = HTTPBasicAuth()

client = MongoClient('mongoserver', 27017)
db = client['example']
col = db['documents']

# TODO:  Will need to replace with actual AD at some point
users = {
    "user": generate_password_hash("p@ssw0rd!")
}

# TODO:  Will need to replace with actual AD at some point
@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

@app.route('/')
@auth.login_required
def index():
    return 'V0.0.1'

@app.route('/document', methods=['POST'])
@auth.login_required
def document():
    data = request.get_json()
    insert_id = col.insert_one(data).inserted_id
    return (str(insert_id), 204)

@app.route('/documents', methods=['GET'])
def documents():
    documents = []
    for document in col.find({}):
        document['_id'] = str(document['_id'])
        documents.append(document)
    return jsonify(documents)

if __name__ == '__main__':
    # Add this line to enable ssl or use a reverse proxy... ur choice
    # app.run(host='0.0.0.0', port='8443', ssl_context=(CERT_PEM_PATH, KEY_PEM_PATH), debug=True)
    app.run(host='0.0.0.0', port='8443', debug=True)
