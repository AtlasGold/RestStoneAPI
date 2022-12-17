from flask import Flask ,request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec,  Response, Request
from model.modelMessage import Message
from tinydb import TinyDB, Query

server =  Flask(__name__)
spec = FlaskPydanticSpec("flask", title= "RestfullStone API")
spec.register(server)
database = TinyDB('database.json')



@server.get('/message')
def get_message():
    ''' Get All Saved Messages. '''
    Query().all
    return database.all()

@server.post('/message')
@spec.validate(body=Request(Message), resp=Response(HTTP_200=Message))
def create_message():
    ''' Add a New Message. '''
    body = request.context.body.dict()  
    database.insert(body)
    return body

server.run()