import pyautogui
import time

pyautogui.FAILSAFE = True

# Give time to prepare
time.sleep(3)

# 1. Open Start Menu
pyautogui.press('win')
time.sleep(1)

# 2. Open Chrome
pyautogui.write('chrome', interval=0.1)
pyautogui.press('enter')

# 3. Wait for browser
time.sleep(5)

# 4. Open Gmail
pyautogui.hotkey('ctrl', 'l')
time.sleep(1)
pyautogui.write('https://mail.google.com', interval=0.05)
pyautogui.press('enter')

# 5. Wait for Gmail to load
time.sleep(8)

# 6. Click Compose button (adjust if needed)
pyautogui.click(125,283)
time.sleep(2)

# 7. Type recipient email
pyautogui.write('genaisocial2026@gmail.com', interval=0.05)
pyautogui.press('tab')

# 8. Type subject
pyautogui.write('Automation Test Mail', interval=0.05)
pyautogui.press('tab')

# 9. Type email body
pyautogui.write(
    'Hello,\n\nThis email was sent using PyAutoGUI automation.\n\nRegards,\nPython Developer',
    interval=0.05
)

# 10. Send email (Ctrl + Enter)
time.sleep(1)
pyautogui.hotkey('ctrl', 'enter')

print("Email sent successfully")
