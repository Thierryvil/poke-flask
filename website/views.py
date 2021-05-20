from flask import Blueprint, render_template, abort
import requests 

views = Blueprint('views', __name__)

@views.route('/')
def home():
    r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1005')
    json_response = r.json()['results']
    
    data = []
    for i in range(len(json_response)):
        poke_name = json_response[i]['name']
        poke_id = (json_response[i]['url'].split('pokemon/')[1]).split('/')[0]         
        data.append({'name' : poke_name, 'id': poke_id})

    return render_template('home.html', data=data)

@views.route('/pokemon/<int:id>', methods=['GET'])
def pokemon(id):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}/') 
    if r.status_code == 200:
        data = r.json()
        return render_template('poke_detail.html', pokemon=data)
    else:
        return abort(404)
