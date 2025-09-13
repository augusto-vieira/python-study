'''
Link do vídeo: https://www.youtube.com/watch?v=9prLBRpwZ78&ab_channel=ODORIZZI
Primeiro Código:
!pip install git+https://github.com/openai/whisper.git
!sudo apt update && sudo apt install ffmpeg
Segundo Código:
!whisper "nome do arquivo aqui.mp3" --model medium
!whisper "TschuggerS01E01.mkv" --model large
whisper é uma IA, que é utilizada para transcrever audio em texto.

whisper "06-TS_1.mp3" --model medium --language German

'''

# https://github.com/openai/whisper/blob/main/README.md
import whisper

model = whisper.load_model("medium")
result = model.transcribe("parte_1.mp3")
#result = model.transcribe("parte_1.mp3", fp16=False, language='English')
print(result["text"])

# instalar as libs
# pip install -r requirements.txt

# Gerar transcrição
# .venv\Scripts\activate

# o whisper consegue traduzir qualquer idioma para o inglês, não traduz para outras linguas.
# whisper parte_1.mp3 --language German --task translate

# whisper parte_1.mp3 --language Portuguese
