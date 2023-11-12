# from flask_restplus import Namespace
from flask import Flask, jsonify, request
from classes.manufactures_connection import *
import requests

querry      = []

api = Flask(__name__)   

@api.route('/', methods=['GET'])
def get_GBIF():
    return jsonify(list(querry))

@api.route('/api/contest', methods=['GET'])
def get():
    factory = ConnectionFactory.connect()
    if factory == None:
        print("Erro")
        return jsonify([])
    print("OI")
    cursor = factory.cursor()
    cursor.execute("SELECT * FROM public.usertable ORDER BY contestnumber ASC, usersitenumber ASC, usernumber ASC ")
    
    return jsonify(list(cursor.fetchone()))

# @api.route('/api/contest/<int:id_c>/tag', methods=['GET'])                Lista as tags associadas à competição dada pelo id_c

# @api.route('/api/contest/<int:id_c>/tag', methods=['POST'])               Uma nova tag associada à competição dada pelo id_c
# @api.route('/api/contest/<int:id_c>/tag/<int:id_t>', methods=['GET'])     Mostra a tag dada pelo id_t no contest id_c
# @api.route('/api/contest/<int:id_c>/tag/<int:id_t>', methods=['PUT'])     Atualiza a tag dada pelo id_t no contest id_c
# @api.route('/api/contest/<int:id_c>/tag/<int:id_t>', methods=['DELETE'])  Remove a tag dada pelo id_t no contest id_c


# def get_search():
#     config = Configuration()
#     condicao_sinalizada.clear()

#     if(len(querry) >= int(config.get_qtd_animais())):
#         print("Limite de animais alcançados, aguarde.")
#         return
    
#     while(True):
#         try:
#             factory = ConnectionFactory.connect()
#             if factory == None:
#                 continue 
#             cursor = factory.cursor()
#             cursor.execute("SELECT id FROM naturae_base WHERE name ILIKE '{}\'".format(base))
#             base_id = cursor.fetchone()
            
#             cursor.execute("""
#                     SELECT id, search_id 
#                     FROM naturae_basesearch 
#                     WHERE base_id = %(id)s AND date_search_end is NULL""",
#                             ({
#                                 'id': base_id[0] # type: ignore
#                             }))
#             base_searchs = cursor.fetchall()
            
#             if len(base_searchs) == 0:
#                 continue
            
#             for (base_search_id, search_id) in base_searchs:
#                 cursor.execute("""
#                         SELECT specie_id 
#                         FROM naturae_search 
#                         WHERE id = %(id)s """,
#                                 ({
#                                     'id': search_id
#                                 }))
#                 specie_id = cursor.fetchone()[0] # type: ignore

#                 cursor.execute("""
#                         SELECT scientific_name 
#                         FROM naturae_specie 
#                         WHERE id = %(id)s """,
#                                 ({
#                                     'id': specie_id
#                                 }))
#                 data = {
#                     "scientificName": cursor.fetchone()[0], # type: ignore
#                     "base_search_id": base_search_id,
#                     "base_id": base_id[0],  # type: ignore
#                     "specie_id":specie_id,
#                 }
#                 if not any(item["scientificName"] == data["scientificName"] for item in querry):
#                     if(len(querry) >= int(config.get_qtd_animais())):
#                         print("Limite de animais alcançados, aguarde.")
#                         break
                    
#                     data["status"] = "esperando envio"
#                     querry.append(data)
                    
#                     thread = threading.Thread(target=envio_imagens, args=(data, config, ), name="Thread envio")
                
#                     # Iniciar as threads
#                     thread.start()
#             condicao_sinalizada.wait(60*60) # 1 H
#             condicao_sinalizada.clear()
            
#         except Exception as e:
#             print(e, end=" - ")
#             if "cursor already closed" in str(e):
#                 print("Perda de contato com o banco de dados")
#                 continue
#             condicao_sinalizada.wait(60) # 1 Min
#             condicao_sinalizada.clear()