from flask import Flask, request, jsonify
from flask_pydantic_spec import (
    FlaskPydanticSpec, Response, Request
)
from tinydb import Query
from model.modelMessage import Message
from model.modelMessagesList import Messages
from model.ModelQuery import QueryMessage, QueryUpdate
from database.database import database

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='RestStone')
spec.register(server)


@server.get('/Messages') 
@spec.validate(
    query=QueryMessage,
    resp=Response(HTTP_200=Messages)
)
def buscar_Messages():
    """Return all Messages."""
    query = request.context.query.dict(exclude_none=True)
    todas_as_Messages = database.search(
        Query().fragment(query)
    )
    return jsonify(
        Messages(
            Messages=todas_as_Messages,
            count=len(todas_as_Messages)
        ).dict()
    )

@server.get('/Messages/<int:id>')
@spec.validate(resp=Response(HTTP_200=Message))
def buscar_Message(id):
    """Get All Messages by Id."""
    try:
        Message = database.search(Query().id == id)[0]
    except IndexError:
        return {'message': 'Message not found!'}, 404
    return jsonify(Message)


@server.post('/Messages')
@spec.validate(
    body=Request(Message), resp=Response(HTTP_201=Message)
)
def inserir_Message():
    """Add an Message ."""
    if(database.search(Query().text == request.context.body.text)):
        return {'message': 'Message alredy exists!'}, 402
    body = request.context.body.dict()
    print(request.context.body.text)
    database.insert(body)
    return body


@server.put('/Messages/<string:text>')
@spec.validate(
    query=QueryUpdate,
    body=Request(Message), resp=Response(HTTP_201=Message)
)
def altera_Message(text):
    """Alter an Message in Database."""
    Message = Query()
    body = request.context.body.dict()
    database.update(body, Message.text == text)
    return jsonify(body)


@server.delete('/Messages/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def deleta_Message(id):
    """Remove an Message of Database."""
    database.remove(Query().id == id)
    return jsonify({})


server.run(host="0.0.0.0")
