import random



dict_musicas = {1: 'Bad Romance', 2: 'Eternal Sunshine', 3: 'Bad idea, right?'}

def get_random_music():
    id, musica = random.choice(list(dict_musicas.items()))
    print(musica)
    if id == 1:
        mostra_info = {'artista':'Lady Gaga', 'album':'The Fame Monster', 'ano': 2009}
        for key,value in mostra_info.items():
            print(f'{key}: {value}')
    if id == 2:
        mostra_info = {'Artista': 'Ariana Grande', 'álbum': 'Eternal Sunshine', 'Ano': 2024}
        for key,value in mostra_info.items():
            print(f'{key}: {value}')
    if id == 3:
        mostra_info = {'Artista': 'Olivia Rodrigo', 'álbum': 'Guts', 'Ano': 2023}
        for key,value in mostra_info.items():
            print(f'{key}: {value}')

get_random_music()
