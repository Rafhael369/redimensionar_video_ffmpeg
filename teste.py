# import os
# import subprocess

# # Define o diretório que contém os vídeos
# diretorio = '/home/rafhael/Vídeos/2023.02.17/'

# # Loop pelos arquivos no diretório
# for arquivo in os.listdir(diretorio):
#     # Verifica se o arquivo é um vídeo
#     if arquivo.endswith('.mp4') or arquivo.endswith('.avi') or arquivo.endswith('.mov'):
#         # Define o caminho completo para o arquivo
#         caminho_completo = os.path.join(diretorio, arquivo)
#         # Define o caminho e o nome de saída para o vídeo redimensionado
#         saida = os.path.join(diretorio, 'redimensionado_' + arquivo)
#         # Executa o comando ffmpeg para redimensionar o vídeo para 1280x720
#         subprocess.call(['ffmpeg', '-i', caminho_completo, '-vf', 'scale=1280:720', '-c:a', 'copy', saida])

import os
import subprocess

# Define o diretório que contém os vídeos
diretorio = '/home/rafhael/Vídeos/2023.02.17/'

# Define as opções de hardware para usar a aceleração por GPU
hwaccel = 'cuvid'
codec = 'h264_nvenc'

# Loop pelos arquivos no diretório
for arquivo in os.listdir(diretorio):
    # Verifica se o arquivo é um vídeo
    if arquivo.endswith('.mp4') or arquivo.endswith('.avi') or arquivo.endswith('.mov'):
        # Define o caminho completo para o arquivo
        caminho_completo = os.path.join(diretorio, arquivo)
        # Define o caminho e o nome de saída para o vídeo redimensionado
        saida = os.path.join(diretorio, 'redimensionado_' + arquivo)
        # Executa o comando ffmpeg para redimensionar o vídeo para 1280x720 com aceleração por GPU
        subprocess.call(['ffmpeg', '-hwaccel', hwaccel, '-i', caminho_completo, '-vf', 'scale=1280:720', '-c:a', 'copy', '-c:v', codec, saida])
