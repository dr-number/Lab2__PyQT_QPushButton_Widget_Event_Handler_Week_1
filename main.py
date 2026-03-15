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
        self.current_image_index = 0
        self.images = []
        self.title = '(название не найдено)'
        self.text_description = {}

        self.initializeUI()
        
    def initializeUI(self):
        '''Настройка графического интерфейса приложения.'''
        self.setGeometry(200, 100, 500, 400)
        self.setWindowTitle(self.title)
        self.setUpMainWindow()
        self.show()
    

    
    def setUpMainWindow(self):
        '''Создание элементов управления в главном окне'''
        main_layout = QVBoxLayout()
        self.text_label = QLabel(self) 
        self.text_label.move(155, 15) 

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setMinimumSize(1000, 600)
        self.image_label.setStyleSheet("border: 1px solid gray;")
        
        self.prev_button = QPushButton("← Назад", self)
        self.next_button = QPushButton("Вперед →", self)
        
        self.prev_button.setFixedSize(100, 30)
        self.next_button.setFixedSize(100, 30)
        
        # Горизонтальный layout для кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Добавление виджетов в основной layout
        main_layout.addWidget(self.image_label)
        main_layout.addWidget(self.text_label)
        main_layout.addLayout(button_layout)
        
        # Установка layout для окна
        self.setLayout(main_layout)
        self.showImage()
    
    def showImage(self, name_file: str, width: int, height: int):
        '''Отображение изображения'''
        try:
            image_path = os.path.join("images", name_file)
            pixmap = QPixmap(image_path)
            
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    width, 
                    height,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.image_label.setPixmap(scaled_pixmap)
                self.text_label.setText(self.text_description.get(name_file, '(описание не найдено)'))

            else:
                self.image_label.setText(f"Не удалось загрузить изображение:\n{self.images[self.current_image_index]}")
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
