# from flask_restplus import Namespace
from flask import Flask, jsonify, request
from classes.manufactures_connection import *
import requests

querry      = []

api = Flask(__name__)   

@api.route('/', methods=['GET'])
def get_GBIF():
    return jsonify(list(querry))

@api.route('/api/contest/<int:id_c>/tag', methods=['GET'])             
def list_tags_id_c(id_c):                                   #  Lista as tags associadas à competição dada pelo id_c
    factory = ConnectionFactory.connect()
    if factory == None:
        return jsonify("Erro")
    
    cursor = factory.cursor()
    
    sql = """
        SELECT tagname
        FROM tagtable
        INNER JOIN contesttable
        ON tagtable.contestnumber=contesttable.contestnumber
        WHERE contesttable.contestnumber = {}
    """.format(id_c)
    
    cursor.execute(sql)
    

    return jsonify(list(cursor.fetchall()))

@api.route('/api/contest/<int:id_c>/tag', methods=['POST'])     # Cadastra uma nova tag associada à competição dada pelo id_c
def add_tags_id_c(id_c):                                    
    date = request.get_json()
    factory = ConnectionFactory.connect()
    
    if factory == None or date is  None:
        return jsonify("Erro")
    
    querry.append(date)
    cursor = factory.cursor()
    sql = """
        INSERT INTO tagtable(tagnumber, tagname, contestnumber)
        VALUES
        ({},'{}',{});
    """.format(date["number"], date["name"], id_c)
    
    cursor.execute(sql)
        
    return jsonify("Cadastrado")

@api.route('/api/contest/<int:id_c>/tag/<int:id_t>', methods=['GET'])   #  Mostra a tag dada pelo id_t no contest id_c
def get_tag_id_c_for_id_t(id_c, id_t):                      
    factory = ConnectionFactory.connect()
    if factory == None:
        return jsonify("Erro")
    
    cursor = factory.cursor()
    
    sql = """
        SELECT tagname 
        FROM tagtable
        INNER JOIN contesttable
        ON tagtable.contestnumber=contesttable.contestnumber
        WHERE contesttable.contestnumber = {} AND tagnumber = {};
    """.format(id_c, id_t)
    
    cursor.execute(sql)
    
    return jsonify(list(cursor.fetchall()))

@api.route('/api/contest/<int:id_c>/tag/<int:id_t>', methods=['PUT'])   #  Atualiza a tag dada pelo id_t no contest id_c
def update_tag_id_c_for_id_t(id_c, id_t):                      
    date = request.get_json()
    factory = ConnectionFactory.connect()
    if factory == None or date is  None:
        return jsonify("Erro")
    
    cursor = factory.cursor()
    
    sql = """
        UPDATE tagtable 
        SET tagname = '{}'
        WHERE contestnumber = {} AND tagnumber = {}
    """.format(date["name"], id_c, id_t)
    
    cursor.execute(sql)
    
    return jsonify("Atualizado")

@api.route('/api/contest/<int:id_c>/tag/<int:id_t>', methods=['DELETE'])  #  Remove a tag dada pelo id_t no contest id_c
def dalete_tag_id_c_for_id_t(id_c, id_t):                      
    factory = ConnectionFactory.connect()
    if factory == None:
        return jsonify("Erro")
    
    cursor = factory.cursor()
    
    sql = """
        DELETE FROM tagtable
        WHERE contestnumber = {} and tagnumber = {}
    """.format(id_c, id_t)
    
    cursor.execute(sql)
    
    return jsonify("Deletado")