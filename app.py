from flask import Flask 
from flask_pydantic_spec import FlaskPydanticSpec,  Response
from model.modelMessage import Message

server =  Flask(__name__)
spec = FlaskPydanticSpec("flask", title= "RestfullStone API")
spec.register(server)

@server.get('/message')
@spec.validate(resp=Response(HTTP_200=Message))
def pegar_pessoa():
    return "Parede Falsa a Frente"

server.run()