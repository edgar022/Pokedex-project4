from flask import Flask, render_template 
import requests, json
from random import randint

url = 'https://pokeapi.co/api/v2/pokemon/'

app = Flask(__name__) 


@app.route("/")
def main():
    names = []
    type = []
    pokeid = []
    sprite = []
    for i in range(0,6):
        num = randint(1, 800)
        pname = str(num)
        pokeid.append(num)
        pokemon_data_url = url + pname
        data = get_pokemon_data(pokemon_data_url)
        res = json.loads(requests.get(pokemon_data_url).text)
        #Nombre del pokemon
        nombre = data.get("name")
        names.append(nombre)
        #Sprite del pokemon
        image = res['sprites']
        image = image['front_default']
        sprite.append(image)
        #Tipo de pokemon
        typePokemon = [types['type']['name'] for types in data['types']]
        type.append(", ".join(typePokemon))

    return render_template('index.html', len = len(names), pokename = names, types = type, number = pokeid, photo = sprite)

def get_pokemon_data(url_pokemon=''):
    pokemon_data = {
        "name": '', 
        "types": ''
    }
    response = requests.get(url_pokemon)
    
    data = response.json()
    pokemon_data['name'] = data['name']
    pokemon_data['types'] = data['types']

    return pokemon_data

  
if __name__ == "__main__":
    app.run(debug=True) 