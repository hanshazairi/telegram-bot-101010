import requests

def get_joke():
  URL = 'https://official-joke-api.appspot.com/random_joke'
  request = requests.get(URL)
  
  if request.status_code == 200:
    data = request.json()
    joke = data['setup'] + '\n\n' + data['punchline']

    return joke
  
  else:
    return f'Error: {request.status_code}'

def get_pokemon(pokemon):
  URL = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
  request = requests.get(URL)

  if request.status_code == 200:
    data = request.json()
    sprite = data['sprites']['front_default']

    return sprite

  else:
    return f'Error: {request.status_code}'