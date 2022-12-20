from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec


server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='RestStone')
spec.register(server)

import api.route.messege

server.run(host="0.0.0.0",port=1234 , debug=True)