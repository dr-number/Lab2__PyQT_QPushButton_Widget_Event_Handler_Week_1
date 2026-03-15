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
        self.setGeometry(200, 50, 500, 400)
        self.setMaximumWidth(500)
        self.setMaximumHeight(400)
        self.setWindowTitle("Об авторе")
        self.setUpMainWindow()
        self.show()

    def __add_info(self, title: str, text: str, text_layout):
        text_label_title = QLabel(title)
        text_label_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        text_label_title.setMaximumWidth(430)
        text_label_title.setWordWrap(True)
        text_layout.addWidget(text_label_title)
        
        text_label_text = QLabel(text)
        text_label_text.setFont(QFont("Arial", 10))
        text_label_text.setMaximumWidth(430)
        text_label_text.setWordWrap(True)
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

        text_label0 = QLabel("Свою фотографию не покажу. Смотрите на смайлик. Он красивый)")
        text_label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label0.setFont(QFont("Arial", 10))
        text_layout.addWidget(text_label0)
        
        text_label1 = QLabel("Ларионов Никита")
        text_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label1.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        text_layout.addWidget(text_label1)

        text_widget2 = QWidget()
        self.text_layout2 = QVBoxLayout(text_widget2)

        button_layout = QHBoxLayout()

        button_ok = QPushButton("ОК", self)
        button_ok.setFixedSize(100, 30)
        button_ok.setToolTip("Нажмите для завершения просмотра")
        button_ok.clicked.connect(self.close_application)

        self.button_more_info = QPushButton("", self)
        self.button_more_info.setFixedSize(100, 30)
        self.show_more_info()

        button_layout.addWidget(button_ok)
        button_layout.addWidget(self.button_more_info)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
        main_layout.addLayout(button_layout)
        main_layout.addWidget(text_widget)
        main_layout.addWidget(text_widget2)
        self.setLayout(main_layout)
        
        # Загружаем изображения
        self.showImage(image_label=self.image_background, name_file="bg.jpg", width=500, height=400, aspect_ratio_mode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.showImage(image_label=self.image_face, name_file="smile.png", width=300, height=300, aspect_ratio_mode=Qt.AspectRatioMode.KeepAspectRatio)

    def close_application(self):
        print("Закрываем приложение...")
        QApplication.quit()

    def __clear_layout(self, layout):
        '''Очистка layout от всех виджетов'''
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def show_more_info(self):
        self.__clear_layout(self.text_layout2)
        self.button_more_info.setText("Подробнее")
        self.button_more_info.setToolTip("Нажмите для просмотра более подробной информации")
        self.button_more_info.clicked.connect(self.show_main_info)
        self.__add_info(
            title="Биография",
            text="Web разработчик (backend, django)",
            text_layout=self.text_layout2
        )
        self.__add_info(
            title="Коммерческий опыт работы:",
            text=(
                "<b>Python:</b> Django, Celery, Redis<br>"
                "<b>C Legacy-кодом</b><br>"
                "<b>Docker; Docker Compose</b><br>"
                "<b>БД:</b> PostgreSQL, MySQL, SQLite<br>"
                "<b>Автоматизацией задач:</b> Bash-скрипты<br>"
                "<b>Java, Kotlin</b><br>"
                "<b>Js</b><br>"
            ),
            text_layout=self.text_layout2
        )
        self.__add_info(
            title="Достижения",
            text=(
                "<b>Оптимизировал</b> скорость генерации документов примерно в 10 раз (с ~30 сек. до ~3 сек.)<br>"
                "<b>Осужествил</b> интеграцию backend с брокерскими системами \"Tradernet by freedom finance\", \"T‑Bank Invest API\", \"Finam Trade API\"<br>"
                "<b>Осужествил</b> интеграцию backend с платежной системой \"Robokassa\"<br>"
                "<b>Разработал</b> систему подписания документов<br>"
                "<b>Разработал</b> мини-систему защиты от DDoS-атак<br>"
                "<b>Осуществил</b> интеграцию с системой расслки смс \"GreenSMS\"<br>"
            ),
            text_layout=self.text_layout2
        )

    def show_main_info(self):
        self.__clear_layout(self.text_layout2)
        self.button_more_info.setText("Назад")
        self.button_more_info.setToolTip("Нажмите для возврата к исходной информации")
        self.button_more_info.clicked.connect(self.show_more_info)
        self.__add_info(
            title="((((Достижения))))",
            text=(
                "хххъъъъъъ"
            ),
            text_layout=self.text_layout2
        )

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
