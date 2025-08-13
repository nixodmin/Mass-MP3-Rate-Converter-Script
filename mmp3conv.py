import os
from pydub import AudioSegment
from pydub.utils import mediainfo

def convert_48000_to_44100(input_path, output_path):
    """Mass MP3 Rate Converter Script 48000Hz to 44100Hz"""
    os.system(f"ffmpeg -i '{input_path}' -ar 44100 -c:a libmp3lame -q:a 2 '{output_path}'")

def main():
    directory = "/ПУТЬ_К/MP3_ФАЙЛАМ"
    temp_suffix = "_converted.mp3"

    for filename in os.listdir(directory):
        if filename.lower().endswith(".mp3"):
            filepath = os.path.join(directory, filename)
            
            # Получаем частоту дискретизации
            audio_info = mediainfo(filepath)
            sample_rate = int(audio_info.get("sample_rate", "44100"))
            
            if sample_rate == 48000:
                print(f"Найден файл с 48000 Гц: {filename}")
                temp_output = os.path.join(directory, f"temp{temp_suffix}")
                final_output = os.path.join(directory, filename)
                
                # Конвертируем во временный файл
                convert_48000_to_44100(filepath, temp_output)
                
                # Удаляем исходный файл и переименовываем временный
                os.remove(filepath)
                os.rename(temp_output, final_output)
                print(f"Конвертирован: {filename} → 44100 Гц")

if __name__ == "__main__":
    main()
