import time
import hashlib
import os
from datetime import datetime
from PIL import ImageGrab
from io import BytesIO
import pygame  # 추가


SOUND_PATH = "/Users/isangsu/Music/효과음/discord-leave-noise.mp3"  # 효과음 파일 경로
pygame.mixer.init()
sound = pygame.mixer.Sound(SOUND_PATH)

default_path = "/Users/isangsu/Pictures/ClipBoardImage"

# SAVE_DIR = "/Volumes/T7_Shield/Files/YOUTUBE/삶을바꾸는깨달음/ImageSources"

SAVE_DIR = input("저장 경로를 입력하세요(미입력시 default): ")

if not SAVE_DIR:  # 입력이 없으면
    SAVE_DIR = default_path  # 기본 경로 설정, 예: "./data"

print(f"지정 경로: {SAVE_DIR}")

CHECK_INTERVAL = 1  # seconds

os.makedirs(SAVE_DIR, exist_ok=True)

def get_clipboard_image():
    try:
        image = ImageGrab.grabclipboard()
        if image is not None:
            return image.convert('RGB')
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
    return None

def get_image_hash(image):
    with BytesIO() as buffer:
        image.save(buffer, format="PNG")
        return hashlib.md5(buffer.getvalue()).hexdigest()

def get_filename():
    return datetime.now().strftime("%y-%m-%d-%H-%M-%S") + ".png"

def main():
    last_hash = None

    while True:
        image = get_clipboard_image()
        if image:
            current_hash = get_image_hash(image)
            if current_hash != last_hash:
                filename = get_filename()
                filepath = os.path.join(SAVE_DIR, filename)
                image.save(filepath)
                print(f"Saved new image: {filepath}")
                sound.play()  # 효과음 재생
                last_hash = current_hash
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()