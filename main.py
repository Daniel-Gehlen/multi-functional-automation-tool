import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_to_md import convert_pdf_to_md
from MP4_to_GIF import convert_mp4_to_gif
from split_gifs import split_gif
from transcribe_videos import VideoTranscriber
from video_to_MP3 import convert_media_to_mp3 as convert_video_to_mp3
from wav_to_mp3 import convert_wav_to_mp3


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Functional Tool")

        # Frame principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=20, pady=20)

        # Label de instrução
        self.label = tk.Label(self.main_frame, text="Escolha uma opção e clique em Gerar:")
        self.label.pack(pady=10)

        # Lista de opções
        self.options = [
            "Converter PDF para Markdown",
            "Converter MP4 para GIF",
            "Dividir GIF",
            "Transcrever Vídeo",
            "Converter Vídeo para MP3",
            "Converter WAV para MP3"
        ]

        # Variável para armazenar a opção selecionada
        self.selected_option = tk.StringVar(value=self.options[0])

        # Menu de opções
        self.option_menu = tk.OptionMenu(self.main_frame, self.selected_option, *self.options)
        self.option_menu.pack(pady=10)

        # Botão Gerar
        self.generate_button = tk.Button(self.main_frame, text="Gerar", command=self.generate)
        self.generate_button.pack(pady=20)

    def generate(self):
        selected = self.selected_option.get()

        if selected == "Converter PDF para Markdown":
            self._convert_pdf_to_markdown()
        elif selected == "Converter MP4 para GIF":
            self._convert_mp4_to_gif()
        elif selected == "Dividir GIF":
            self._split_gif()
        elif selected == "Transcrever Vídeo":
            self._transcribe_video()
        elif selected == "Converter Vídeo para MP3":
            self._convert_video_to_mp3()
        elif selected == "Converter WAV para MP3":
            self._convert_wav_to_mp3()

    def _convert_pdf_to_markdown(self):
        # Abrir caixa de diálogo para selecionar o arquivo PDF
        pdf_path = filedialog.askopenfilename(
            title="Selecione o arquivo PDF",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not pdf_path:
            messagebox.showwarning("Aviso", "Nenhum arquivo PDF selecionado!")
            return

        # Abrir caixa de diálogo para escolher onde salvar o arquivo Markdown
        md_path = filedialog.asksaveasfilename(
            title="Salvar como Markdown",
            defaultextension=".md",
            filetypes=[("Markdown Files", "*.md")]
        )

        if not md_path:
            messagebox.showwarning("Aviso", "Nenhum local para salvar o arquivo Markdown selecionado!")
            return

        # Converter PDF para Markdown
        result = convert_pdf_to_md(pdf_path, md_path)
        messagebox.showinfo("Resultado", result)

    def _convert_mp4_to_gif(self):
        # Abrir caixa de diálogo para selecionar o arquivo MP4
        mp4_path = filedialog.askopenfilename(
            title="Selecione o arquivo MP4",
            filetypes=[("MP4 Files", "*.mp4")]
        )

        if not mp4_path:
            messagebox.showwarning("Aviso", "Nenhum arquivo MP4 selecionado!")
            return

        # Abrir caixa de diálogo para escolher onde salvar o arquivo GIF
        gif_path = filedialog.asksaveasfilename(
            title="Salvar como GIF",
            defaultextension=".gif",
            filetypes=[("GIF Files", "*.gif")]
        )

        if not gif_path:
            messagebox.showwarning("Aviso", "Nenhum local para salvar o arquivo GIF selecionado!")
            return

        # Converter MP4 para GIF
        result = convert_mp4_to_gif(mp4_path, gif_path)
        messagebox.showinfo("Resultado", result)

    def _split_gif(self):
        # Abrir caixa de diálogo para selecionar o arquivo GIF
        gif_path = filedialog.askopenfilename(
            title="Selecione o arquivo GIF",
            filetypes=[("GIF Files", "*.gif")]
        )

        if not gif_path:
            messagebox.showwarning("Aviso", "Nenhum arquivo GIF selecionado!")
            return

        # Dividir GIF
        result = split_gif(gif_path)
        messagebox.showinfo("Resultado", result)

    def _transcribe_video(self):
        # Abrir caixa de diálogo para selecionar o arquivo de vídeo
        video_path = filedialog.askopenfilename(
            title="Selecione o arquivo de vídeo",
            filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov *.flv *.wmv")]
        )

        if not video_path:
            messagebox.showwarning("Aviso", "Nenhum arquivo de vídeo selecionado!")
            return

        # Transcrever vídeo
        transcriber = VideoTranscriber()
        result = transcriber.transcribe_video(video_path)
        messagebox.showinfo("Resultado", result)

    def _convert_video_to_mp3(self):
        # Abrir caixa de diálogo para selecionar o arquivo de vídeo
        video_path = filedialog.askopenfilename(
            title="Selecione o arquivo de vídeo",
            filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov *.flv *.wmv")]
        )

        if not video_path:
            messagebox.showwarning("Aviso", "Nenhum arquivo de vídeo selecionado!")
            return

        # Abrir caixa de diálogo para escolher onde salvar o arquivo MP3
        mp3_path = filedialog.asksaveasfilename(
            title="Salvar como MP3",
            defaultextension=".mp3",
            filetypes=[("MP3 Files", "*.mp3")]
        )

        if not mp3_path:
            messagebox.showwarning("Aviso", "Nenhum local para salvar o arquivo MP3 selecionado!")
            return

        # Converter vídeo para MP3
        result = convert_video_to_mp3(video_path, mp3_path)  # Passa ambos os caminhos
        messagebox.showinfo("Resultado", result)

    def _convert_wav_to_mp3(self):
        # Abrir caixa de diálogo para selecionar o arquivo WAV
        wav_path = filedialog.askopenfilename(
            title="Selecione o arquivo WAV",
            filetypes=[("WAV Files", "*.wav")]
        )

        if not wav_path:
            messagebox.showwarning("Aviso", "Nenhum arquivo WAV selecionado!")
            return

        # Abrir caixa de diálogo para escolher onde salvar o arquivo MP3
        mp3_path = filedialog.asksaveasfilename(
            title="Salvar como MP3",
            defaultextension=".mp3",
            filetypes=[("MP3 Files", "*.mp3")]
        )

        if not mp3_path:
            messagebox.showwarning("Aviso", "Nenhum local para salvar o arquivo MP3 selecionado!")
            return

        # Converter WAV para MP3
        result = convert_wav_to_mp3(wav_path, mp3_path)
        messagebox.showinfo("Resultado", result)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
