# server.py
from flask import Flask, render_template, send_file, request, redirect
import cv2
import os
from datetime import datetime
from threading import Thread
import time


PORT = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PORT, GPIO.OUT)
GPIO.output(PORT, GPIO.HIGH)


app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


image_list = []
camera = cv2.VideoCapture(1)

# Объект для выделения движения
fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=50, detectShadows=False)

# Функция для захвата изображений с камеры с выделением движения
def capture_images():
    global image_list
    while True:
        ret, frame = camera.read()
        if ret:
            # Применяем выделение движения
            fgmask = fgbg.apply(frame)

            # Проверяем, есть ли движение
            if cv2.countNonZero(fgmask) > 500000:  # Изменено пороговое значение
                # Генерируем уникальное имя для изображения
                GPIO.OUTPUT(PORT, GPIO.LOW)
                time.sleep(5)
                GPIO.output(PORT, GPIO.HIGH)
                filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                # Сохраняем изображение
                cv2.imwrite(filepath, frame)
                image_list.append(filename)

# Запуск потока для захвата изображений
capture_thread = Thread(target=capture_images)
capture_thread.daemon = True
capture_thread.start()

# Обработчик для загрузки изображения с камеры
@app.route('/upload', methods=['POST'])
def upload():
    return render_template('index.html', image_list=image_list)

# Обработчик для отображения изображений
@app.route('/')
def index():
    return render_template('index.html', image_list=image_list)

# Обработчик для открытия и скачивания изображения
@app.route('/image/<filename>')
def get_image(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
