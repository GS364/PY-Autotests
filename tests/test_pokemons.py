import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "af5467b303a405945437695ff2d7c905"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = "28963"

def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params={"trainer_id":TRAINER_ID})
    assert response.status_code == 200 

def test_trainers():
    response = requests.get(url= f'{URL}/trainers')
    assert response.status_code == 200

def my_trainer():
    response = requests.get(url= f'{URL}/trainers', params= {"trainer_id":TRAINER_ID})
    assert response.json()['trainer_name']==['Геназавр']

'''@pytest. mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '279358')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value'''