import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Se extrae la primera definición disponible
        return data[0]["meanings"][0]["definitions"][0]["definition"]
    return "Definición no encontrada."

def get_synonyms(word):
    url = f"https://api.datamuse.com/words?rel_syn={word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            # Se juntan los sinónimos en una cadena
            return ", ".join([item['word'] for item in data])
        return "No se encontraron sinónimos."
    return "Error al buscar sinónimos."

def get_youtube_video(word):
    # Función simplificada: se retorna la URL de búsqueda en YouTube
    return f"https://www.youtube.com/results?search_query={word}+explanation"
