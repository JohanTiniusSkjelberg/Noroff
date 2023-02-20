import pyautogui
import keyboard 
from PIL import Image
import pytesseract
import time
# text = input()
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
keyboard.wait("enter")
ga = pyautogui.position()
screenshot = pyautogui.screenshot(region=(ga[0],ga[1], 1200,350))
screenshot = screenshot.convert('L')
# Save the screenshot to a file
screenshot.save('screenshot.png')
# Load the screenshot file as an image
image = Image.open('screenshot.png')
text = pytesseract.image_to_string(image)
time.sleep(2)
pyautogui.write(text.replace("\n"," "),interval=0.08)
# Print the extracted text
print(text.replace("\n"," "))
# pyautogui.click()