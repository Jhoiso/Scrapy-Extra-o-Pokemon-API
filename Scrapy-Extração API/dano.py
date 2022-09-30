from functools import reduce
import json
from statistics import mean

from mrjob.job import MRJob
from mrjob.step import MRStep

#Mapper criado para pegar a chave 'Dano' e trazer todos os danos tomados por cada tipo, assim, vai ser feita uma média de todos os danos tomados com o
#reducer

class ContadorDeJoaos(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapperDano, reducer=self.reducerDano),
        ]

    def mapperDano(self, _, arq_jsonlines):
        poekdex = json.loads(arq_jsonlines)
        for chave, valor in poekdex["Dano"].items():
            yield chave, float(valor)

    def reducerDano(self, chave, valores):
        yield chave, mean(valores)


if __name__ == '__main__':
    ContadorDeJoaos.run()
