import  requests

link= "http://localhost:4040/api/" 
    
if __name__ == "__main__": 
    
    #  Lista as tags associadas à competição dada pelo id_c 
    requisicao = requests.get(link+"problem/2004/tag")
    
    # Cadastra uma nova tag associada à competição dada pelo id_c
    # requisicao = requests.post(link + "user/1000/tag", json= {"value": "online"})
    # requisicao = requests.get(link+"user/1000/tag")
    
    #  Mostra a tag dada pelo id_t no contest id_c
    # requisicao = requests.post(link + "contest/2/tag/1")
    
    #  Atualiza a tag dada pelo id_t no contest id_c
    # requisicao = requests.put(link + "contest/1/tag/3", json= {"value": "alteracao"})
    
    #  Remove a tag dada pelo id_t no contest id_c
    # requisicao = requests.delete(link + "/user/1/tag/2")    
    # requisicao = requests.delete(link + "/contest/1/tag/2")    
    
    if requisicao.status_code == 200:
        print(requisicao.json())