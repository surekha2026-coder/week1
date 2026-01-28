import pyautogui
import time

# Fail-safe: move mouse to top-left to stop script
pyautogui.FAILSAFE = True

# Give time to prepare
time.sleep(2)

# 1. Open Start menu
pyautogui.press('win')
time.sleep(1)

# 2. Open browser (Chrome)
pyautogui.write('chrome', interval=0.1)
pyautogui.press('enter')

# 3. Wait for browser to open
time.sleep(5)

# 4. Focus address bar
pyautogui.hotkey('ctrl', 'l')
time.sleep(1)

# 5. Type search query
pyautogui.write('south africa vs australia score', interval=0.1)
pyautogui.press('enter')

# 6. Wait for search results
time.sleep(5)

# 7. Click first search result (coordinates may vary)
pyautogui.click(400, 350)

print("Search completed and first link clicked")
