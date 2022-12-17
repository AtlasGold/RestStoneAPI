from flask import Flask , request
from flask_pydantic_spec import FlaskPydanticSpec,  Response, Request
from model.modelMessage import Message

server =  Flask(__name__)
spec = FlaskPydanticSpec("flask", title= "RestfullStone API")
spec.register(server)



@server.get('/message')
def get_message():
    return "Parede Falsa a Frente"

@server.post('/message')
@spec.validate(body=Request(Message), resp=Response(HTTP_200=Message))
def create_message():
    ''' Add a New Message '''
    body = request.context.body.dict()  
    return body

server.run()