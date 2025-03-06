import os
import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def find_image():
    """
    Procura a primeira imagem no diretório atual.
    Retorna o nome do arquivo ou None se não encontrar.
    """
    supported_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    for file in os.listdir('.'):
        if any(file.lower().endswith(ext) for ext in supported_extensions):
            return file
    return None

def create_animation_from_image():
    # Busca automaticamente a imagem no diretório
    image_file = find_image()
    if not image_file:
        print("Nenhuma imagem encontrada no diretório atual.")
        return

    # Carrega a imagem
    image = cv2.imread(image_file)

    if image is None:
        print("Erro ao carregar a imagem.")
        return

    # Configurações do vídeo
    height, width, _ = image.shape
    output_file = "animated_image.mp4"
    fps = 30
    duration = 5  # segundos
    total_frames = fps * duration

    # Prepara o vídeo
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    for i in range(total_frames):
        # Efeito de zoom suave
        scale = 1 + (0.1 * (i / total_frames))
        center_x, center_y = width // 2, height // 2
        zoomed_image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

        # Calcula os cortes para centralizar a imagem
        crop_x1 = (zoomed_image.shape[1] - width) // 2
        crop_y1 = (zoomed_image.shape[0] - height) // 2
        crop_x2 = crop_x1 + width
        crop_y2 = crop_y1 + height

        # Centraliza a imagem redimensionada no quadro
        zoomed_cropped = zoomed_image[crop_y1:crop_y2, crop_x1:crop_x2]

        video.write(zoomed_cropped)

    video.release()

    print(f"Animação criada com sucesso! Arquivo salvo como {output_file}")

if __name__ == "__main__":
    create_animation_from_image()
