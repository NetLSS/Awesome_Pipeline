import pyautogui
import os

save_path = os.path.expanduser("~/Desktop")  # 데스크탑에 저장
img = pyautogui.screenshot()
img.save(os.path.join(save_path, "test_screenshot.png"))
print("저장 완료")