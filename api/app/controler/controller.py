# from flask_restplus import Namespace
from flask import Flask, jsonify, request
from classes.manufactures_connection import *
import requests

querry      = []

api = Flask(__name__)   

@api.route('/', methods=['GET'])
def get_GBIF():
    return jsonify(list(querry))

@api.route('/api/<string:entityType>/<int:entityId>/tag', methods=['GET'])     #  Lista as tags associadas à competição dada pelo id_c
def list_tags_id_c(entityType, entityId):
    
    factory = ConnectionFactory.connect()
    if factory == None:
        return jsonify("Erro")
    
    cursor = factory.cursor()
    
    sql = """
        SELECT {0}name
        FROM {0}table
        WHERE {0}table.{0}number = {1}
    """.format(entityType, entityId)
    
    cursor.execute(sql)
    
    try:
        name = cursor.fetchone()[0] # type:ignore
    except:
       return jsonify("Sem registo na {}table".format(entityType))
    
    sql = """
        SELECT id, value
        FROM tagtable
        WHERE name = '{}'
    """.format(name)
    
    cursor.execute(sql)
    
    tags = [ 
        {
            "id": id,
            "name": name,
            "value": value
        }for (id, value) in cursor.fetchall() # type:ignore
    ]

    dic = {
        "entityTag": [
            {
                "entityType": entityType,
                "entityId": entityId,
                "tag": tags
            }
        ]
    }
    return jsonify(dic)

@api.route('/api/<string:entityType>/<int:entityId>/tag', methods=['POST'])     # Cadastra uma nova tag associada à competição dada pelo id_c
def add_tags_id_c(entityType, entityId):                                    
    date = request.get_json()
    factory = ConnectionFactory.connect()
    
    if date is None:
       return jsonify("Falta o envio do valor da tag")
    
    if factory == None:
        return jsonify("Erro - conexao com banco")
    
    querry.append(date)
    cursor = factory.cursor()
    
    sql = """
        SELECT {0}name
        FROM {0}table
        WHERE {0}table.{0}number = {1}
    """.format(entityType, entityId)
    
    cursor.execute(sql)
    
    try:
        name = cursor.fetchone()[0] # type:ignore
    except:
       return jsonify("Sem registo na {}table".format(entityType))
    
    
    sql = """
        INSERT INTO tagtable(name, value)
        VALUES
        ('{}','{}');
    """.format(name, date["value"])
    
    cursor.execute(sql)
    
    return jsonify("Cadastrado")

@api.route('/api/<string:entityType>/<int:entityId>/tag/<int:tagId>', methods=['GET'])   #  Mostra a tag dada pelo id_t no entityType id_c
def get_tag_id_c_for_id_t(entityType, entityId, tagId):                      
    factory = ConnectionFactory.connect()
    if factory == None:
        return jsonify("Erro")
    
    cursor = factory.cursor()
    
    sql = """
        SELECT {0}name
        FROM {0}table
        WHERE {0}table.{0}number = {1}
    """.format(entityType, entityId)
    
    cursor.execute(sql)
    
    try:
        name = cursor.fetchone()[0] # type:ignore
    except:
       return jsonify("Sem registo na {}table".format(entityType))
    
    sql = """
        SELECT id, value
        FROM tagtable
        WHERE name = '{}' and id = {}
    """.format(name, tagId)
    
    cursor.execute(sql)
    
    tag = cursor.fetchone() # type:ignore
    
    tags ={
        "id": tag[0],       # type:ignore
        "name": name,
        "value": tag[1]     # type:ignore
    }

    dic = {
        "entityTag": [
            {
                "entityType": entityType,
                "entityId": entityId,
                "tag": tags
            }
        ]
    }
    return jsonify(dic)

@api.route('/api/<string:entityType>/<int:id_c>/tag/<int:id_t>', methods=['PUT'])   #  Atualiza a tag dada pelo id_t no entityType id_c
def update_tag_id_c_for_id_t(entityType, id_c, id_t):                      
    date = request.get_json()
    factory = ConnectionFactory.connect()
    if factory == None or date is  None:
        return jsonify("Erro")
    
    cursor = factory.cursor()
    
    sql = """
        UPDATE tagtable 
        SET tagname = '{}'
        WHERE {}number = {} AND tagnumber = {}
    """.format(entityType, date["name"], id_c, id_t)
    
    cursor.execute(sql)
    
    return jsonify("Atualizado")

@api.route('/api/<string:entityType>/<int:id_c>/tag/<int:id_t>', methods=['DELETE'])  #  Remove a tag dada pelo id_t no entityType id_c
def dalete_tag_id_c_for_id_t(entityType, id_c, id_t):                      
    factory = ConnectionFactory.connect()
    if factory == None:
        return jsonify("Erro")
    
    cursor = factory.cursor()
    
    sql = """
        DELETE FROM tagtable
        WHERE {}number = {} and tagnumber = {}
    """.format(entityType, id_c, id_t)
    
    cursor.execute(sql)
    
    return jsonify("Deletado")