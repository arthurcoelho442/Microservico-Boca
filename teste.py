import  requests

link= "http://localhost:4040/api/contest/" 
    
if __name__ == "__main__": 
    
    #  Lista as tags associadas à competição dada pelo id_c 
    requisicao = requests.get(link+"2/tag")
    
    # Cadastra uma nova tag associada à competição dada pelo id_c
    # requisicao = requests.post(link + "2/tag", json= {"number": 2, "name": "teste"})
    
    #  Mostra a tag dada pelo id_t no contest id_c
    # requisicao = requests.post(link + "2/tag/1")
    
    #  Atualiza a tag dada pelo id_t no contest id_c
    # requisicao = requests.put(link + "2/tag/2", json= {"name": "alteracao"})
    
    #  Remove a tag dada pelo id_t no contest id_c
    # requisicao = requests.delete(link + "2/tag/2")    
    
    if requisicao.status_code == 200:
        print(requisicao.json())