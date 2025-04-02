import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    # Si se encuentra la palabra, se convierte la entrada a JSON
    if response.status_code == 200:
        # Convierte la palabra a JSON
        # Se verifica si la respuesta contiene datos
        data = response.json()
        # Se extrae la primera definición disponible buscando en un diccionario en base a la estructura de la API
        return data[0]["meanings"][0]["definitions"][0]["definition"]
    return "Definition not found."

def get_synonyms(word):
    url = f"https://api.datamuse.com/words?rel_syn={word}"
    response = requests.get(url)
    # Si se encuentra la palabra, se convierte la entrada a JSON
    if response.status_code == 200:
        data = response.json()
        if data:
            # Se juntan los sinónimos en una cadena
            return ", ".join([item['word'] for item in data])
        return "No synonyms found."
    return "Error searching for synonyms."

def get_youtube_videos(word):
    # Se retorna la URL de búsqueda en YouTube
    return f"https://www.youtube.com/results?search_query={word}+explanation"
