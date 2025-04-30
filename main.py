import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "USER_TOKEN"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
BODY_REG = {
    "trainer_token": TOKEN,
    "email": "LOGIN@mail.ru",
    "password": "PASSWORD",
}
BODY_CONF = {"trainer_token": TOKEN}
BODY_CREATE_POK = {"name": "generate", "photo_id": -1}


"""response_reg = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = BODY_REG)
print(response_reg.text)"""

"""response_conf = requests.post(url=f'{URL}/trainers/confirm_email', headers= HEADER, json = BODY_CONF)
print(response_conf.text)"""

response_create_pok = requests.post(
    url=f"{URL}/pokemons", headers=HEADER, json=BODY_CREATE_POK
)
print(response_create_pok.text)

pokemon_id = response_create_pok.json()["id"]
BODY_CHANGE_NAME = {"pokemon_id": pokemon_id, "name": "generate", "photo_id": -1}
BODY_IN_POKEBALL = {"pokemon_id": pokemon_id}

response_change_name = requests.put(
    url=f"{URL}/pokemons", headers=HEADER, json=BODY_CHANGE_NAME
)
print(response_change_name.json())

response_in_pokeball = requests.post(
    url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=BODY_IN_POKEBALL
)
print(response_in_pokeball.json())
