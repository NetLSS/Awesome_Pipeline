import time
import hashlib
import os
from datetime import datetime
from PIL import ImageGrab
from io import BytesIO
import pygame  # 추가
import pyautogui  # 추가


SOUND_PATH = "/Users/isangsu/Music/효과음/discord-leave-noise.mp3"  # 효과음 파일 경로
pygame.mixer.init()
sound = pygame.mixer.Sound(SOUND_PATH)

default_path = "/Users/isangsu/Pictures/ClipBoardImage"

# SAVE_DIR = "/Volumes/T7_Shield/Files/YOUTUBE/삶을바꾸는깨달음/ImageSources"

print("""
저장 경로를 입력하세요(미입력시 default): 
0. 직접입력
1. 깨달음이머무르는곳 (/Volumes/T7_Shield/Files/YOUTUBE/깨달음이머무는곳/images)
2. 말씀의샘 (/Volumes/T7_Shield/Files/YOUTUBE/말씀의샘/imageSources)
3. 진리의 서원(/Volumes/T7_Shield/Files/YOUTUBE/진리의서원/images)
""")


SAVE_DIR = input("저장 경로를 입력하세요(미입력시 default): ")

print(f"input {SAVE_DIR}")

if SAVE_DIR == "0":  # 입력이 없으면
    SAVE_DIR = input("저장 경로를 입력하세요(미입력시 default): ")
    if not SAVE_DIR:  # 입력이 없으면
        SAVE_DIR = default_path  # 기본 경로 설정, 예: "./data"
if SAVE_DIR == "1":
    SAVE_DIR = "/Volumes/T7_Shield/Files/YOUTUBE/깨달음이머무는곳/images"
elif SAVE_DIR == "2":
    SAVE_DIR = "/Volumes/T7_Shield/Files/YOUTUBE/말씀의샘/imageSources"
elif SAVE_DIR == "3":
    SAVE_DIR = "/Volumes/T7_Shield/Files/YOUTUBE/진리의서원/images"
else: 
    SAVE_DIR = default_path  # 기본 경로 설정, 예: "./data"


print(f"지정 경로: {SAVE_DIR}")

CHECK_INTERVAL = 0.2  # seconds

반복횟수 = input("반복 횟수를 지정하세요: (default:60)")

if not 반복횟수:  # 입력이 없으면
    반복횟수 = 60  # 기본 경로 설정, 예: "./data"
else:
    # 숫자형으로 변환
    try:
        반복횟수 = int(반복횟수)
    except ValueError:
        print("잘못된 입력입니다. 기본값 60으로 설정합니다.")
        반복횟수 = 60

os.makedirs(SAVE_DIR, exist_ok=True)


# 🖱 좌상단 좌표 입력
input("\n[STEP 1] 좌상단 위치로 마우스를 이동한 후, Enter 키를 누르세요.")
x1, y1 = pyautogui.position()
print(f"좌상단 좌표: ({x1}, {y1})")

# 🖱 우하단 좌표 입력
input("\n[STEP 2] 우하단 위치로 마우스를 이동한 후, Enter 키를 누르세요.")
x2, y2 = pyautogui.position()
print(f"우하단 좌표: ({x2}, {y2})")

print("10초 후 스크린샷을 시작합니다...")
time.sleep(10)

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

def click_click():

    time.sleep(0.1)

    # 좌상단 우클릭
    pyautogui.click(x1, y1, button='right')

    time.sleep(0.1)

    # 우하단 좌클릭
    pyautogui.click(x2, y2, button='left')

    time.sleep(2.5)


def main():
    last_hash = None

    for i in range(반복횟수):
        click_click()
        
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
        pyautogui.press('left')   # 화살표 누르기

if __name__ == "__main__":
    main()