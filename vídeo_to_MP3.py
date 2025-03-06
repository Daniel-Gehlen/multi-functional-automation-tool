import os
import subprocess

def convert_media_to_mp3(input_path, output_path):
    """
    Converte arquivo de mídia para MP3.
    """
    try:
        # Verifica se o arquivo de entrada existe
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")

        # Comando FFmpeg para conversão
        comando = [
            "ffmpeg",
            "-i", input_path,       # Entrada
            "-vn",                  # Sem vídeo
            "-acodec", "libmp3lame", # Codec MP3
            "-q:a", "2",            # Qualidade alta
            output_path             # Saída
        ]

        # Executa o comando
        result = subprocess.run(comando, 
                                capture_output=True, 
                                text=True, 
                                check=False)
        
        # Verifica se o comando falhou
        if result.returncode != 0:
            raise RuntimeError(f"Falha na conversão: {result.stderr}")

        # Verifica se o MP3 foi criado
        if not os.path.exists(output_path):
            raise FileNotFoundError(f"MP3 não foi criado: {output_path}")

        return f"Conversão concluída: {output_path}"

    except Exception as e:
        raise RuntimeError(f"Erro ao processar {input_path}: {e}")
