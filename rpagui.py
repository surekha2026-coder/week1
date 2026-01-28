import time
import pyautogui
#mouse operations
'''pyautogui.click(100,100)
time.sleep(3)
pyautogui.rightClick(200,200)
time.sleep(10)
x,y=pyautogui.position()
print(f"Current mouse position: x={x}, y={y}")
time.sleep(5)
pyautogui.moveTo(300,300,duration=2)
time.sleep(5)
pyautogui.moveRel(100,0,duration=2)
time.sleep(5)
pyautogui.doubleClick(100,100)
time.sleep(5)
pyautogui.drag(100,100,duration=2)
time.sleep(5)
pyautogui.scroll(500)   
time.sleep(5)
pyautogui.scroll(-500) 
time.sleep(5)
#keyboard operations
pyautogui.write("Hello, this is automated typing using pyautogui")
time.sleep(5)
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('ctrl','a')
time.sleep(5)   
#pyautogui.hotkey('alt','f4')
'''
#image recognition and screenshot
#location=pyautogui.locateOnScreen('notepad_icon.png')
#print(location) 
#screenshot=pyautogui.screenshot()   
#screenshot.save("screenshot.png")
time.sleep(5)
print(pyautogui.size())

