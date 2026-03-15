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
from PyQt6.QtGui import QPixmap, QFont

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

    def __add_info(self, title: str, text: str, text_layout):
        text_label_title = QLabel(title)
        text_label_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        text_layout.addWidget(text_label_title)
        
        text_label_text = QLabel(text)
        text_label_text.setFont(QFont("Arial", 10))
        text_layout.addWidget(text_label_text)
    
    def setUpMainWindow(self):
        '''Создание элементов управления в главном окне'''
        # Создаем главный вертикальный контейнер
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 20)  # Отступ снизу для текста
        main_layout.setSpacing(10)
        
        # Создаем контейнер для изображений
        images_widget = QWidget()
        images_layout = QVBoxLayout(images_widget)
        images_layout.setContentsMargins(0, 0, 0, 0)
        images_layout.setSpacing(0)
        
        # Контейнер для фонового изображения и смайлика
        self.image_background = QLabel()
        self.image_background.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_background.setFixedSize(500, 400)
        
        self.image_face = QLabel()
        self.image_face.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_face.setFixedSize(300, 300)
        self.image_face.move(100, 50)  # Позиционируем внутри фонового виджета
        
        # Создаем контейнер для наложения изображений
        overlay_widget = QWidget()
        overlay_widget.setFixedSize(500, 400)
        overlay_layout = QVBoxLayout(overlay_widget)
        overlay_layout.setContentsMargins(0, 0, 0, 0)
        
        # Добавляем оба изображения в один контейнер
        overlay_layout.addWidget(self.image_background)
        self.image_face.setParent(overlay_widget)
        
        images_layout.addWidget(overlay_widget)
        
        # Добавляем контейнер с изображениями в главный макет
        main_layout.addWidget(images_widget)

        # СОЗДАЕМ ТЕКСТОВЫЕ ПОЛЯ (ВЕРТИКАЛЬНОЕ РАСПОЛОЖЕНИЕ)
        text_widget = QWidget()
        text_layout = QVBoxLayout(text_widget)
        text_layout.setSpacing(10)
        text_layout.setContentsMargins(30, 20, 30, 20)

        # Текстовое поле 0
        self.text_label0 = QLabel("Свою фотографию не покажу. Смотрите на смайлик. Он красивый)")
        self.text_label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label0.setFont(QFont("Arial", 10))
        text_layout.addWidget(self.text_label0)
        
        # Текстовое поле 1
        self.text_label1 = QLabel("Ларионов Никита")
        self.text_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label1.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        text_layout.addWidget(self.text_label1)

        self.__add_info(
            title="Биография",
            text="Web разработчик (backend, django)",
            text_layout=text_layout
        )
        
    
        
        main_layout.addWidget(text_widget)
        self.setLayout(main_layout)
        
        # Загружаем изображения
        self.showImage(image_label=self.image_background, name_file="bg.jpg", width=500, height=400, aspect_ratio_mode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.showImage(image_label=self.image_face, name_file="smile.png", width=300, height=300, aspect_ratio_mode=Qt.AspectRatioMode.KeepAspectRatio)




    def showImage(self, image_label: QLabel, name_file: str, width: int, height: int, aspect_ratio_mode):
        '''Отображение изображения'''
        try:
            pixmap = QPixmap(os.path.join("images", name_file))
            
            if not pixmap.isNull():
                image_label.setPixmap(pixmap.scaled(
                    width, 
                    height,
                    aspect_ratio_mode,
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
