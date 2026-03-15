import sys
import os
import json
import re
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from traceback import format_exc
from PyQt6.QtWidgets import QMessageBox


class AboutMe(QWidget):

    def __init__(self):
        '''Инициализация слайдера'''
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        '''Настройка графического интерфейса приложения.'''
        self.setGeometry(200, 100, 500, 400)
        self.setWindowTitle("Об авторе")
        self.setUpMainWindow()
        self.show()
    
    def setUpMainWindow(self):
        '''Создание элементов управления в главном окне'''
    

        self.image_background = QLabel(self)
        self.image_background.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_background.setGeometry(0, 0, 500, 400)  # Устанавливаем размер как у окна

        self.image_face = QLabel(self)
        self.image_face.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_face.setGeometry(100, 50, 300, 300)  # Позиционируем смайлик

       
        self.showImage(image_label=self.image_background, name_file="bg.jpg", width=500, height=400)
        self.showImage(image_label=self.image_face, name_file="smile.png", width=300, height=300)


    def showImage(self, image_label: QLabel, name_file: str, width: int, height: int):
        '''Отображение изображения'''
        try:
            pixmap = QPixmap(os.path.join("images", name_file))
            
            if not pixmap.isNull():
                image_label.setPixmap(pixmap.scaled(
                    width, 
                    height,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                ))

            else:
                image_label.setText(f"Не удалось загрузить изображение:\n{name_file}")
                return False
                
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}\n{format_exc()}")
            return False
        
        return True


# Запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AboutMe()
    sys.exit(app.exec())
