import os
from PIL import Image, ImageSequence
import imageio
import numpy as np

def normalize_frames(frames):
    # Determina o tamanho máximo (largura e altura) de todos os quadros
    max_width = max(frame.width for frame in frames)
    max_height = max(frame.height for frame in frames)
    
    normalized_frames = []
    for frame in frames:
        # Cria uma nova imagem com fundo transparente (ou branco) no tamanho máximo
        new_frame = Image.new("RGBA", (max_width, max_height), (255, 255, 255, 0))
        # Centraliza o frame original na nova imagem
        new_frame.paste(frame, (0, 0))
        normalized_frames.append(new_frame)
    
    return normalized_frames

def split_gif(gif_path):
    try:
        # Carrega o GIF
        with Image.open(gif_path) as gif:
            # Extrai os quadros
            frames = [frame.convert("RGBA") for frame in ImageSequence.Iterator(gif)]
            
            # Normaliza os quadros para terem o mesmo tamanho
            frames = normalize_frames(frames)
            
            # Divide os quadros em duas partes
            half = len(frames) // 2
            part1_frames = frames[:half]
            part2_frames = frames[half:]
            
            # Define os nomes dos arquivos de saída
            base_name = os.path.splitext(gif_path)[0]
            part1_path = f"{base_name}_part1.gif"
            part2_path = f"{base_name}_part2.gif"
            
            # Salva cada parte
            duration = gif.info.get('duration', 100)  # Duração padrão de 100ms por quadro se não especificado
            imageio.mimsave(part1_path, [np.array(f) for f in part1_frames], duration=duration / 1000)
            imageio.mimsave(part2_path, [np.array(f) for f in part2_frames], duration=duration / 1000)
            
            return f"GIF dividido em: {part1_path} e {part2_path}"
    
    except Exception as e:
        return f"Erro ao processar o arquivo {gif_path}: {str(e)}"
