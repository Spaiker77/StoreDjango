# Skystore - Интернет-магазин цифровых товаров

Skystore - это платформа для продажи цифровых товаров, включая плагины, шаблоны кода, веб-приложения и микросервисы.

## 🚀 Основные возможности

- Каталог цифровых товаров
- Страница контактов с формой обратной связи
- Адаптивный дизайн (mobile-first)
- Современный UI с использованием Bootstrap 5

## 📦 Установка и настройка

### Предварительные требования
- Python 3.9+
- pip
- virtualenv (рекомендуется)

### Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/skystore.git
   cd skystore
Создайте и активируйте виртуальное окружение:

bash
python -m venv venv
# Для Windows:
venv\Scripts\activate
# Для Linux/MacOS:
source venv/bin/activate
Установите зависимости:

bash
pip install -r requirements.txt

Примените миграции:
bash
python manage.py migrate

Создайте суперпользователя (опционально):
bash
python manage.py createsuperuser

Запустите сервер разработки:
bash
python manage.py runserver

Откройте в браузере:
text
http://localhost:8000
🏗️ Структура проекта
text
skystore/
├── config/               # Основные настройки Django
│   ├── settings.py       # Конфигурация приложения
│   ├── urls.py           # Главные URL-адреса
│   └── ...
├── catalog/              # Приложение каталога
│   ├── migrations/       # Миграции базы данных
│   ├── templates/        # HTML шаблоны
│   ├── admin.py          # Настройки админки
│   ├── apps.py           # Конфиг приложения
│   ├── models.py         # Модели данных
│   ├── urls.py           # URL-адреса приложения
│   └── views.py          # Контроллеры
├── static/               # Статические файлы
│   ├── css/              # CSS стили
├── manage.py             # Управление Django
└── requirements.txt      # Зависимости Python

🌐 Используемые технологии
Backend:
Python 3.9+
Django 4.2
Django Templates

Frontend:
Bootstrap 5
HTML5
CSS3

Инструменты разработки:
Git
pip
virtualenv

🛠️ Разработка
Запуск в режиме разработки
bash
python manage.py runserver

Создание миграций
bash
python manage.py makemigrations
python manage.py migrate

Запуск тестов
bash
python manage.py test

Сбор статических файлов (для production)
bash
python manage.py collectstatic

📄 Лицензия
Этот проект распространяется под лицензией MIT. См. файл LICENSE для получения дополнительной информации.

🤝 Контрибьютинг
Форкните проект

Создайте ветку для вашей фичи (git checkout -b feature/AmazingFeature)

Зафиксируйте изменения (git commit -m 'Add some AmazingFeature')

Запушьте ветку (git push origin feature/AmazingFeature)

Откройте Pull Request

### Рекомендации по использованию:
1. Замените `ваш-username`, `ваш.email@example.com` и другие placeholder'ы на свои данные
2. Добавьте логотип проекта в `static/images/logo.png` (размер примерно 200x200px)
3. Для красивого отображения Markdown можно использовать:
   - В VS Code: Ctrl+Shift+V (Windows/Linux) или Cmd+Shift+V (Mac)
   - На GitHub: автоматически рендерится при просмотре файла
4. Для добавления бейджей (версия Python, статус сборки и т.д.) можно использовать [shields.io](https://shields.io/)