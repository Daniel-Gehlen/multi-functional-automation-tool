from pydub import AudioSegment
import os

def convert_wav_to_mp3(wav_path, mp3_path):
    """
    Converte um arquivo WAV para MP3.
    """
    try:
        # Verifica se o arquivo WAV existe
        if not os.path.exists(wav_path):
            raise FileNotFoundError(f"Arquivo WAV não encontrado: {wav_path}")

        # Se o arquivo MP3 já existe, exclua-o antes de criar um novo
        if os.path.exists(mp3_path):
            print(f"Removendo arquivo MP3 existente: {mp3_path}")
            os.remove(mp3_path)
        
        # Converte o arquivo WAV para MP3
        print(f"Convertendo: {wav_path} para {mp3_path}")
        audio = AudioSegment.from_wav(wav_path)
        audio.export(mp3_path, format="mp3")
        
        return f"Conversão concluída: {mp3_path}"

    except Exception as e:
        return f"Erro ao converter {wav_path}: {e}"
