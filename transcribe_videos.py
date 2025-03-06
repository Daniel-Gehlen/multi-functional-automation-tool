import os
import subprocess
import speech_recognition as sr
from pydub import AudioSegment


class VideoTranscriber:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def extract_audio(self, video_path):
        """
        Extrai o áudio de um arquivo de vídeo usando FFmpeg.
        """
        try:
            if not os.path.exists(video_path):
                raise FileNotFoundError(f"Arquivo de vídeo não encontrado: {video_path}")

            audio_path = os.path.splitext(video_path)[0] + ".wav"

            comando = [
                "ffmpeg",
                "-i", video_path,
                "-vn",
                "-acodec", "pcm_s16le",
                "-ar", "16000",
                "-ac", "1",
                audio_path
            ]

            result = subprocess.run(comando, capture_output=True, text=True, check=False)
            
            if result.returncode != 0:
                raise RuntimeError(f"Falha na extração de áudio: {result.stderr}")

            if not os.path.exists(audio_path):
                raise FileNotFoundError(f"Áudio não foi criado: {audio_path}")

            return audio_path

        except Exception as e:
            raise RuntimeError(f"Erro ao extrair áudio: {e}")

    def transcribe_audio(self, audio_path, language='pt-BR'):
        """
        Transcreve o áudio usando reconhecimento de fala.
        """
        try:
            audio = AudioSegment.from_wav(audio_path)
            chunk_length = 30 * 1000  # 30 segundos
            chunks = [audio[i:i+chunk_length] for i in range(0, len(audio), chunk_length)]

            full_transcript = []

            for i, chunk in enumerate(chunks):
                chunk_path = f"temp_chunk_{i}.wav"
                chunk.export(chunk_path, format="wav")

                try:
                    with sr.AudioFile(chunk_path) as source:
                        audio_chunk = self.recognizer.record(source)
                        transcript = self.recognizer.recognize_google(audio_chunk, language=language)
                        full_transcript.append(transcript)
                
                except sr.UnknownValueError:
                    full_transcript.append(f"[Chunk {i+1}: Áudio não reconhecido]")
                except sr.RequestError as e:
                    full_transcript.append(f"[Chunk {i+1}: Erro na solicitação de transcrição: {e}]")
                
                os.remove(chunk_path)

            return " ".join(full_transcript)

        except Exception as e:
            raise RuntimeError(f"Erro ao transcrever áudio: {e}")

    def transcribe_video(self, video_path):
        """
        Processa um vídeo: extrai áudio e transcreve.
        """
        try:
            audio_path = self.extract_audio(video_path)
            transcript = self.transcribe_audio(audio_path)
            
            txt_path = os.path.splitext(video_path)[0] + "_transcricao.txt"
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(transcript)
            
            os.remove(audio_path)

            return f"Transcrição salva em: {txt_path}"

        except Exception as e:
            return f"Erro ao processar {video_path}: {e}"
