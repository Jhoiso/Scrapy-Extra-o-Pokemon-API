import jsonlines
import json

# Arquivo que converte o .json gerado para um jasonlines, para facilitar a leitura no mapper e do reducer

with open('pokemon.json', 'r') as f:
    json_data = json.load(f)

with jsonlines.open("pokemon.jl", 'w') as writer:
    writer.write_all(json_data)
 