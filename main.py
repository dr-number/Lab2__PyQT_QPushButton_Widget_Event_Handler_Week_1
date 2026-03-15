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


class ImageSlider(QWidget):

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
        main_layout = QVBoxLayout()

        self.image_background = QLabel(self)
        self.image_background.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_background.setMinimumSize(400, 350)

        self.image_face = QLabel(self)
        self.image_face.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_face.setMinimumSize(400, 350)
        
        # Добавление виджетов в основной layout
        main_layout.addWidget(self.image_background)
        main_layout.addWidget(self.image_face)
        
        # Установка layout для окна
        self.setLayout(main_layout)
        self.showImage(image_label=self.image_background, name_file="bg.jpg", width=400, height=350)
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
    window = ImageSlider()
    sys.exit(app.exec())
