# Multi-Functional Automation Tool

This project is a **Multi-Functional Automation Tool** designed to automate various file conversion and processing tasks. It provides a user-friendly interface built with **Tkinter** and integrates multiple Python libraries to handle different file formats and tasks.

---

## Features

The tool supports the following functionalities:

1. **Convert PDF to Markdown**: Extract text from PDF files and save it as Markdown.
2. **Convert MP4 to GIF**: Convert video files (MP4) to animated GIFs.
3. **Split GIFs**: Split a GIF into two parts.
4. **Transcribe Videos**: Extract audio from video files and transcribe it to text.
5. **Convert Video to MP3**: Extract audio from video files and save it as MP3.
6. **Convert WAV to MP3**: Convert WAV audio files to MP3 format.

---

## Technologies Used

### Programming Language
- **Python 3**: The core language used for scripting and automation.

### Libraries and Tools
- **Tkinter**: For building the graphical user interface (GUI).
- **PyPDF2**: For reading and extracting text from PDF files.
- **MoviePy**: For video and GIF processing (e.g., MP4 to GIF conversion).
- **Pydub**: For audio processing (e.g., WAV to MP3 conversion).
- **SpeechRecognition**: For transcribing audio from video files.
- **FFmpeg**: A backend tool used by MoviePy and Pydub for handling multimedia files.
- **Imageio**: For reading and writing image and video files.
- **Markdownify**: For converting HTML to Markdown (used in PDF to Markdown conversion).

---

## Use Cases

This tool is ideal for:
1. **Content Creators**: Convert videos to GIFs or extract audio from videos for use in multimedia projects.
2. **Developers**: Automate repetitive tasks like file format conversions.
3. **Researchers**: Transcribe audio from video lectures or interviews.
4. **Documentation Teams**: Convert PDF documents to Markdown for easier editing and version control.
5. **Audio Engineers**: Convert audio files between formats (e.g., WAV to MP3).

---

## How to Use

### Prerequisites
1. **Python 3**: Ensure Python 3 is installed on your system.
2. **FFmpeg**: Install FFmpeg for handling multimedia files.
   - On Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```
   - On Windows: Download from [FFmpeg's official website](https://ffmpeg.org/) and add it to your system PATH.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Tool
1. Start the application:
   ```bash
   python3 main.py
   ```

2. Use the GUI to select the desired functionality and follow the prompts.

---

## Code Structure

- **`main.py`**: The main script that initializes the Tkinter GUI and handles user interactions.
- **`pdf_to_md.py`**: Converts PDF files to Markdown.
- **`MP4_to_GIF.py`**: Converts MP4 videos to GIFs.
- **`split_gifs.py`**: Splits a GIF into two parts.
- **`transcribe_videos.py`**: Transcribes audio from video files.
- **`vídeo_to_MP3.py`**: Extracts audio from video files and saves it as MP3.
- **`wav_to_mp3.py`**: Converts WAV audio files to MP3.

---

## Contributing

Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to the developers of the Python libraries used in this project.
- Special thanks to the open-source community for providing tools and resources.

---
