import requests

def obtener_contenido_web(url):
    try:
        # Realizamos la petición GET
        response = requests.get(url)
        
        # Verificamos si la petición fue exitosa
        if response.status_code == 200:
            print("La petición fue exitosa!")
            print("Contenido de la página:")
            print(response.text[:500])  # Mostrar los primeros 500 caracteres del contenido
        else:
            print(f"Error: La petición no fue exitosa. Código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ha ocurrido un error al hacer la petición: {e}")



def obtener_datos_pokemon(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        nombre = data['name']
        id = data['id']
        peso = data['weight']
        altura = data['height']
        tipos = [t['type']['name'] for t in data['types']]
        
        print(f"Nombre: {nombre}")
        print(f"ID: {id}")
        print(f"Peso: {peso}")
        print(f"Altura: {altura}")
        print(f"Tipos: {', '.join(tipos)}")
        
        # Obtener cadena de evolución
        url_especie = data['species']['url']
        response_especie = requests.get(url_especie)
        response_especie.raise_for_status()
        data_especie = response_especie.json()
        
        url_cadena_evolucion = data_especie['evolution_chain']['url']
        response_evolucion = requests.get(url_cadena_evolucion)
        response_evolucion.raise_for_status()
        data_evolucion = response_evolucion.json()
        
        cadena_evolucion = []
        cadena = data_evolucion['chain']
        while cadena:
            cadena_evolucion.append(cadena['species']['name'])
            cadena = cadena['evolves_to'][0] if cadena['evolves_to'] else None
        
        print(f"Cadena de Evolución: {', '.join(cadena_evolucion)}")
        
        # Obtener juegos
        juegos = [juego['version']['name'] for juego in data['game_indices']]
        print(f"Juegos: {', '.join(juegos)}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos del Pokémon: {e}")

if __name__ == "__main__":
    
    obtener_contenido_web("https://www.mercedes-benz.es/")
    pokemon = input("Introduce el nombre o número del Pokémon: ")
    obtener_datos_pokemon(pokemon)