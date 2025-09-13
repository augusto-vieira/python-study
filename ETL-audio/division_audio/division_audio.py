import os
from pydub import AudioSegment

def dividir_audio(arquivo_audio, duracao_em_minutos=10):
    # Carregar o áudio
    audio = AudioSegment.from_file(arquivo_audio)
    
    # Duração máxima por segmento em milissegundos
    duracao_max_segmento = duracao_em_minutos * 60 * 1000
    
    # Número de partes
    total_duracao = len(audio)
    partes = (total_duracao // duracao_max_segmento) + 1
    
    # Definir a pasta de saída
    output_dir = "transformar"

    # Verifica se a pasta de saída existe, se não, cria a pasta
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(partes):
        inicio = i * duracao_max_segmento
        fim = min((i + 1) * duracao_max_segmento, total_duracao)
        
        # Dividir o áudio
        segmento = audio[inicio:fim]
        
        # Criar o caminho completo para o arquivo de saída
        output_file = os.path.join(output_dir, f"parte_{i + 1}.mp3")
        
        # Salvar o segmento no diretório de saída
        segmento.export(output_file, format="mp3")
        print(f"Parte {i + 1} salva: {output_file}")

# Exemplo de uso
arquivo = "audio.wav"
dividir_audio(arquivo)
