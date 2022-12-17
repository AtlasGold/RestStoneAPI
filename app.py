from flask import Flask 

server =  Flask(__name__)

@server.get('/pessoas')
def pegar_pessoa():
    return "teste"

server.run()