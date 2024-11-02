from modelos.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Média de avaliação'} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {str(restaurante.media_avaliacao()).ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')
    
    @property
    def ativo(self):
        return 'Sim'.title() if self._ativo else 'Não'.title() #Getter
   
    def ativar_restaurante(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if 1.0 <= nota <= 5.0:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao) 
        else:
            return 'Insira uma nota de 1.0 a 5.0'

    def media_avaliacao(self):
        if not self._avaliacao:
            return '-' 
        soma_das_notas = sum(avaliacao.nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media 
        

        

            
     

