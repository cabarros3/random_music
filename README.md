# Música Aleatória do Dia
A ideia é fazer uma aplicação que todo dia mostre uma música aleatória, o app também deve mostrar informações adicionais sobre a música, como: nome do artista, álbum, ano de lançamento link para o youtube/spotify.
## MVP
Inicialmente criar um app que mostre aleatóriamente uma música que foi pré-selecionada e guardada dentro de uma lista, também deve mostrar informações adicionais sobre a música.
## Como fiz?
- Criar um dicionário com as música selecionadas da seguinte forma `{1:'nome_da_musica_1}'`
- Criar uma função `get_random_music()` e dentro dessa função por meio do método `random.choice()` pegar uma música eleatória do diconário
- 


# Metas para o futuro da aplicação
- consumir API
- Uma aplicação Django
- Mostrar na interface
- Player de música
- Salvar a música todos os dias em que for acessado
- Periodicamente criar uma playlist com as músicas
- Não permitir que seja recebida mais de uma música por dia
