# Scrapy-Extra-o-Pokemon-API
Trabalho 6º semestre, Ciência de Dados - Ciência da Computação 

## Site o qual os pokémons foram extraidos:
https://www.serebii.net/pokedex/001.shtml

## Rodando o main.py
Main.py é o arquivo de scrapy, onde todos os dados serão extraidos do site.
Para gerar o arquivo .json com todos os 151 pokémons, digite o seguinte código no terminal:
  scrapy runspider main.py pokemon.json
  
## Rodando o Conversor.py
Criei o convertor para facilitar a leitura do arquivo, já que inseri um dicionário como valor.
Para gerar o arquivo .jl com:
  python conversor.py pokemon.json
  
## Rodando os Mappers e Reducers
Existem 2 arquivos, dano.py e tipo.py, esses arquivos são um mapreduce:

### dano.py
Este arquivo irá ter como saída, no terminal, uma lista de todos os tipos de dano existentes no pokémon, e ao lado, a média desses danos
Esse 'dano' seria o *dano tomado por cada tipo*, já que no pokémon existe um peso ao pokémon receber um dano.
  python dano.py pokemon.jl
  
### tipo.py
Este arquivo irá ter como saída, no terminal, uma lista de todos os tipos de pokémon, e ao lado, a contagem de vezes em que o tipo apareceu, ou seja, quantos pokémons de cada tipo existem, dentre os 151 analisados.
  python tipó.py pokemon.jl

