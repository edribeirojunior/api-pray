from flask import Flask, request, Response
import json
from database.db import initialize_db
from database.models import Pray

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/api-pray'
}

initialize_db(app)

@app.route('/prays', methods=['GET'])
def get_movies():
    names = []
    for i in Pray.objects:
        names.append(i.name)
    return Response(json.dumps(names), mimetype='application/json', status=200)

@app.route('/prays', methods=['POST'])
def add_movie():
    body = request.get_json()
    pray = Pray(**body).save()
    name = pray.name
    return {'name': str(name)}, 200

@app.route('/prays/<name>', methods=['PUT'])
def update_pray(name):
    body = request.get_json()
    Pray.objects.get(name=name).update(**body)
    return '', 200

@app.route('/prays/<name>', methods=['DELETE'])
def delete_pray(name):
    Pray.objects.get(name=name).delete()
    return '', 200

@app.route('/prays/<name>')
def get_movie(name):
    prays = Pray.objects.get(name=name).to_json()
    return Response(prays, mimetype='application/json', status=200)

app.run()