import os
import subprocess

def extract_audio(input_file, output_file):
    try:
        # Definir a pasta de saída
        output_dir = "extrair_audio"

        # Verifica se a pasta de saída existe, se não, cria a pasta
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Cria o caminho completo do arquivo de saída dentro da pasta "extrair_audio"
        output_file_path = os.path.join(output_dir, output_file)

        # Comando FFmpeg para extrair e converter o áudio para MP3
        command = [
            "ffmpeg",
            "-i", input_file,   # Arquivo de entrada
            "-vn",              # Ignora o vídeo
            "-map", "0:1",      # Seleciona a faixa de áudio (ajuste conforme necessário)
            "-acodec", "libmp3lame",  # Converte o áudio para MP3
            "-q:a", "2",        # Define a qualidade do MP3 (2 = alta qualidade)
            output_file_path    # Caminho do arquivo de saída
        ]
        subprocess.run(command, check=True)
        print(f"Áudio extraído e convertido com sucesso: {output_file_path}")
        
    except subprocess.CalledProcessError as e:
        print("Erro ao extrair ou converter áudio:", e)

# Exemplo de uso
input_video = "DicaProfsTC.mkv"  # Substitua pelo nome do seu arquivo de vídeo
output_audio = "audio.wav"  # Substitua pelo nome desejado para o áudio (audio.mp3 ou audio.wav)
extract_audio(input_video, output_audio)
