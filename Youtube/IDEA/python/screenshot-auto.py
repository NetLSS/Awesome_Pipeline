import pyautogui
import time
import os
import mss
import mss.tools

# ⏺ 저장 경로 입력
save_path = input("스크린샷을 저장할 폴더 경로를 입력하세요 (예: /Users/yourname/Desktop/screenshots): ").strip()

if not os.path.exists(save_path):
    os.makedirs(save_path)
    print(f"폴더가 없어서 생성했습니다: {save_path}")

# 🖱 좌상단 좌표 입력
input("\n[STEP 1] 좌상단 위치로 마우스를 이동한 후, Enter 키를 누르세요.")
x1, y1 = pyautogui.position()
print(f"좌상단 좌표: ({x1}, {y1})")

# 🖱 우하단 좌표 입력
input("\n[STEP 2] 우하단 위치로 마우스를 이동한 후, Enter 키를 누르세요.")
x2, y2 = pyautogui.position()
print(f"우하단 좌표: ({x2}, {y2})")

# 📐 캡처 영역 계산
x_start = min(x1, x2)
y_start = min(y1, y2)
width = abs(x2 - x1)
height = abs(y2 - y1)
region = {'top': y_start, 'left': x_start, 'width': width, 'height': height}

print(f"\n✅ 캡처 영역: {region}")
print("10초 후 스크린샷을 시작합니다...")
time.sleep(10)

# 📸 스크린샷 루프
with mss.mss() as sct:
    for i in range(386):
        print(f"반복 {i+1} / 386")

        filename = os.path.join(save_path, f"screenshot_{i+1:03}.png")
        sct_img = sct.grab(region)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename)

        print(f"{i+1}/386 저장됨: {filename}")

        time.sleep(0.1)            # 캡처 후 잠시 대기
        pyautogui.press('left')   # 왼쪽 화살표 누르기
        time.sleep(15)           # 15초 대기

# import pyautogui
# import time
# import os
# import subprocess
# import mss
# import mss.tools

# # ⏺ 저장 경로 입력
# save_path = input("스크린샷을 저장할 폴더 경로를 입력하세요 (예: /Users/yourname/Desktop/screenshots): ").strip()

# if not os.path.exists(save_path):
#     os.makedirs(save_path)
#     print(f"폴더가 없어서 생성했습니다: {save_path}")

# # 🖱 좌상단 좌표 입력
# input("\n[STEP 1] 좌상단 위치로 마우스를 이동한 후, Enter 키를 누르세요.")
# x1, y1 = pyautogui.position()
# print(f"좌상단 좌표: ({x1}, {y1})")

# # 🖱 우하단 좌표 입력
# input("\n[STEP 2] 우하단 위치로 마우스를 이동한 후, Enter 키를 누르세요.")
# x2, y2 = pyautogui.position()
# print(f"우하단 좌표: ({x2}, {y2})")

# # 📐 캡처 영역 계산
# x_start = min(x1, x2)
# y_start = min(y1, y2)
# width = abs(x2 - x1)
# height = abs(y2 - y1)
# region = (x_start, y_start, width, height)

# print(f"\n✅ 캡처 영역: {region}")
# print("3초 후 스크린샷을 시작합니다...")
# time.sleep(3)


# for i in range(386):
#     print(f"반복 {i+1} / 386")  # 현재 반복 횟수 출력 (선택 사항)
#     # pyautogui.click()
#     # pyautogui.hotkey('command', 'shift', '5')  # 3. cmd + shift + 5

#     # pyautogui.keyDown('command')
#     # pyautogui.keyDown('shift')
#     # pyautogui.press('5')
#     # pyautogui.keyUp('shift')
#     # pyautogui.keyUp('command')
#     # pyautogui.keyUp('5')

#     # time.sleep(0.1)                      # 화면 녹화 창 뜨는 시간 약간 기다리기

#     # pyautogui.press('enter')            # 4. 엔터

#     screenshot = pyautogui.screenshot(region=region)
#     filename = os.path.join(save_path, f"screenshot_{i+1:03}.png")
#     screenshot.save(filename)

#     subprocess.run(["screencapture", "-x", filename])

#     print(f"{i+1}/386 저장됨: {filename}")

#     time.sleep(0.1)                        # 엔터 후 작업 안정화 시간

#     pyautogui.press('left')             # 1. 왼쪽 화살표

#     time.sleep(2.0)                        # 2. 2초 대기
    
