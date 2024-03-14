import random

dict_musicas = {
    1: {'titulo': 'Bad Romance', 'artista': 'Lady Gaga', 'album': 'The Fame Monster', 'ano': 2009},
    2: {'titulo': 'Eternal Sunshine', 'artista': 'Ariana Grande', 'album': 'Eternal Sunshine', 'ano': 2024},
    3: {'titulo': 'Bad idea, right?', 'artista': 'Olivia Rodrigo', 'album': 'Guts', 'ano': 2023}
}

def mostrar_informacoes_musica(musica_info):
    for key, value in musica_info.items():
        print(f'{key.capitalize()}: {value}')

def get_random_music():
    id, musica_info = random.choice(list(dict_musicas.items()))
    print(musica_info['titulo']) # acessa chave do dicionário gerado na função musica_info() 
    mostrar_informacoes_musica(musica_info) # mostra musica aleatória 

get_random_music()