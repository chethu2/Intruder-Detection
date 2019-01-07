from flask import request, url_for
from flask_api import FlaskAPI
from flask import jsonify
from flask import json
from flask import Response
from flask import send_from_directory, send_file
from flask_cors import CORS
import plivo
import database

app = FlaskAPI(__name__)
CORS(app)
cassandraOperations = database.CassandraOperations()

@app.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    name = data['name']
    if(cassandraOperations.checkIfUserRegistered(name)):
        return jsonify({'result':'team '+name+' already registered'})
    else:
        registerToDB(name,'Registered')
        return jsonify({'result':"team "+name+" registered successfully!!"})

@app.route('/update',methods=['POST'])
def update():
    data = request.get_json()
    teamName = data['name']
    time = data['time']
    url = data['url']
    if(updateDB(teamName,time,url)):
        return jsonify({'result':'data updated successfully to cloud'})
    return jsonify({'result':'unauthorised user'})

def registerToDB(name,status):
    query = "INSERT INTO workshop.student_entries(teamName,status) values('"+name+"','"+status+"');"
    return cassandraOperations.executeQuery(query)

def updateDB(name,time,url):
    if(cassandraOperations.checkIfUserRegistered(name)):
        query = "UPDATE workshop.intruder_log set time='"+time+"',url='"+url+"' WHERE teamName='"+name+"';"
        cassandraOperations.executeQuery(query)
        return True
    return False

if __name__ == '__main__':
#    cassandraOperations = database.CassandraOperations()
    cassandraOperations.createSession('host')
    cassandraOperations.setLogger('INFO')
    cassandraOperations.createKeyspaceIfNotExists('workshop')
    cassandraOperations.executeQuery('CREATE TABLE IF NOT EXISTS student_entries(teamName text PRIMARY KEY, status text);')
    cassandraOperations.executeQuery('CREATE TABLE IF NOT EXISTS intruder_log(teamName text PRIMARY KEY, time text, url text);')
    app.run(host='0.0.0.0', port=50010)
