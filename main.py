import cv2
import numpy as np

width = 100
height = 100
duration = 3

video = cv2.VideoWriter('text.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
background = np.zeros((height, width, 3), dtype=np.uint8)
background.fill(255)
text = input('Введите текст: ')
font = cv2.FONT_HERSHEY_COMPLEX
font_scale = 1
font_color = (0, 0, 0)
text_size, _ = cv2.getTextSize(text, font, font_scale, 1)
x = width

speed = int(text_size[0] / duration)

while x > -text_size[0]:
    frame = background.copy()
    cv2.putText(frame, text, (x, int(height / 2)), font, font_scale, font_color, 2)
    video.write(frame)
    x -= speed


video.release()
