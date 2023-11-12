# from flask_restplus import Namespace
from flask import Flask, jsonify, request

import requests

querry      = []


api = Flask(__name__)   

@api.route('/', methods=['GET'])
def get_GBIF():
    return jsonify(list(querry))