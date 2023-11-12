import os

class Configuration:
    def __init__(self):
        self.qtd_process        = os.environ["QUANTIDADE_PROCESSOS"]

    def set_qtd_process(self, qtd_process):
        self.qtd_process = qtd_process
        
    def get_qtd_process(self):
        return int(self.qtd_process)