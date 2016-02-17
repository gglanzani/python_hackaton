from flask import Flask
from flask_restful import Api

from resources.fraud import Fraud

app = Flask(__name__)
api = Api(app, errors=errors)


api.add_resource(Fraud, '/is_fraud/<int:account>/')

if __name__ == '__main__':
    app.run(debug=True, port=5005)
