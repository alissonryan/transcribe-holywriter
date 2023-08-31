# Importando bibliotecas necessárias
import os
import subprocess

# Instalando a biblioteca whisper
os.system('pip install git+https://github.com/openai/whisper.git')

# Instalando a biblioteca youtube_dl
os.system('sudo pip install git+https://github.com/ytdl-org/youtube-dl.git@master#egg=youtube_dl')

# Perguntando ao usuário o link do YouTube
link_youtube = input("Coloque aqui o seu link do youtube: ")

# Informando ao usuário que o download está sendo feito
print("Estamos fazendo o download do áudio do seu vídeo, aguarde um momento.")

# Rodando o comando para baixar o vídeo em formato mp3
command = f'youtube-dl -x --audio-format mp3 {link_youtube}'
process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Recuperando o nome do arquivo .mp3 baixado
output_lines = process.stdout.decode('utf-8').split("\n")
for line in output_lines:
    if "[ffmpeg] Destination:" in line:
        file_name = line.split(": ")[1].strip()

# Informando ao usuário que o vídeo está sendo transcrito
print("Aguarde um momento, seu vídeo está sendo traduzido...")

# Rodando o comando para transcrever o arquivo mp3
command_translate = f'whisper --task translate --language Portuguese --model large "{file_name}"'
os.system(command_translate)

# Informando ao usuário que o vídeo foi transcrito com sucesso
print("Seu vídeo foi traduzido com sucesso.")
