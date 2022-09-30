from functools import reduce
import json

from mrjob.job import MRJob
from mrjob.step import MRStep

#Mapper criado para pegar a chave 'Tipo' e trazer todos os danos tomados por cada tipo, assim, com o reducer, vai ser feita uma contagem de quantas vezes o tipo apareceu
#reducer

class ContadorDeJoaos(MRJob):

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer)]

    def mapper(self, _, arq_jsonlines):
        pokedex = json.loads(arq_jsonlines)
        tipo = pokedex['Tipo']
        yield tipo, 1

    def reducer(self, chave, valores):
        yield chave, sum(valores)


if __name__ == '__main__':
    ContadorDeJoaos.run()
