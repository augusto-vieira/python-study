import os
import subprocess
from pathlib import Path

# Caminhos para as pastas de entrada e saída
entrada_dir = Path("entrada_audio")
saida_dir = Path("saida_transcrita")

# Verificar e criar a pasta de saída, se necessário
saida_dir.mkdir(exist_ok=True)

# Verificar se a pasta de entrada existe
if not entrada_dir.exists():
    raise FileNotFoundError(f"A pasta de entrada '{entrada_dir}' não existe.")

# Listar arquivos .mp3 na pasta de entrada
arquivos_mp3 = list(entrada_dir.glob("*.mp3"))

if not arquivos_mp3:
    print("Nenhum arquivo .mp3 encontrado na pasta de entrada.")
else:
    print(f"{len(arquivos_mp3)} arquivo(s) .mp3 encontrado(s). Iniciando transcrição...")

# Processar cada arquivo
for arquivo in arquivos_mp3:
    caminho_entrada = arquivo.resolve()
    print(f"Processando: {arquivo.name}")
    
    # Definir o comando para executar o Whisper
    comando = [
        "whisper", str(caminho_entrada),
        "--model", "small",   # tipos: tiny base small medium large turbo
        "--language", "Portuguese", 
        "--output_dir", str(saida_dir)
    ]
    
    try:
        # Executar o comando via subprocess
        subprocess.run(comando, check=True)
        print(f"Transcrição concluída para {arquivo.name}. Arquivo gerado em {saida_dir}.")
    
    except subprocess.CalledProcessError as e:
        print(f"Erro ao transcrever o áudio {arquivo.name}: {e}")
    except Exception as e:
        print(f"Erro inesperado ao processar {arquivo.name}: {e}")

print("Processo concluído.")


'''
python -m venv .venv
.\.venv\Scripts\activate
pip install git+https://github.com/openai/whisper.git
whisper --help
'''