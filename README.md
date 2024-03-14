# Música Aleatória do Dia
A ideia é fazer uma aplicação que todo dia mostre uma música aleatória, o app também deve mostrar informações adicionais sobre a música, como: nome do artista, álbum, ano de lançamento link para o youtube/spotify.
## Versão 1.0
Inicialmente criar um programa que mostre aleatóriamente uma música pré-selecionada e guardada dentro de uma lista, também deve mostrar informações adicionais sobre a música.
## Como fiz?
- Criar um dicionário com as música selecionadas da seguinte forma `{1:'nome_da_musica_1}'`
- Criar uma função `get_random_music()` e dentro dessa função por meio do método `random.choice()` pegar uma música eleatória do diconário
- Criar um `if` para identificar o `id` da música e a partir do `id` mostrar informações sobre a música.

## Versão 1.1
Para melhorar o código foi preciso utilizar **dicionários aninhandos**, onde uma chave do dicionário receber como valor um outro dicionário com uma subchave e um valor. Também foi preciso quebra a função `random_music` em duas, uma para mostrar as informações denominada `show_music_information()` e a `random_music()`.

# Metas para o futuro da aplicação
- consumir API
- Uma aplicação Django
- Mostrar na interface
- Player de música
- Salvar a música todos os dias em que for acessado
- Periodicamente criar uma playlist com as músicas
- Não permitir que seja recebida mais de uma música por dia
