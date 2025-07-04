# Skystore - Интернет-магазин цифровых товаров


Skystore - это платформа для продажи цифровых товаров, включая программное обеспечение, видеоигры и музыкальные файлы.

## 🚀 Основные возможности

- Каталог товаров с категориями (Видеоигры, ПО, Музыка)
- Адаптивный интерфейс с улучшенной навигацией
- Страница контактов с динамическими данными
- Локальные статические файлы Bootstrap 5
- Админ-панель для управления контентом

## 📦 Установка и настройка

### Предварительные требования
- Python 3.9+
- PostgreSQL 13+
- pip

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
Настройте базу данных:

Создайте БД PostgreSQL

Заполните .env по примеру .env.example

Примените миграции:

bash
python manage.py migrate
Загрузите тестовые данные:

bash
python manage.py loaddata catalog/fixtures/category.json
python manage.py loaddata catalog/fixtures/product.json
Создайте суперпользователя:

bash
python manage.py createsuperuser
Запустите сервер:

bash
python manage.py runserver
Откройте в браузере: http://localhost:8000

🏗️ Структура проекта
text
StoreDjango/
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
│   ├── css/              # Локальные CSS файлы Bootstrap
│   └── images/           # Изображения
├── manage.py             # Управление Django
└── requirements.txt      # Зависимости Python
🌐 Используемые технологии
Backend:

Python 3.9+

Django 5.0

PostgreSQL

Frontend:

Bootstrap 5 (локальные файлы)

HTML5, CSS3

Адаптивный дизайн

Инструменты:

Git

pip

virtualenv

🛠️ Команды разработки
Команда	Описание
python manage.py runserver	Запуск сервера разработки
python manage.py makemigrations	Создание миграций
python manage.py migrate	Применение миграций
python manage.py collectstatic	Сбор статических файлов
python manage.py test	Запуск тестов
📄 Лицензия
Этот проект распространяется под лицензией MIT. См. файл LICENSE для получения дополнительной информации.

🤝 Контрибьютинг
Форкните проект

Создайте ветку для вашей фичи (git checkout -b feature/AmazingFeature)

Зафиксируйте изменения (git commit -m 'Add some AmazingFeature')

Запушьте ветку (git push origin feature/AmazingFeature)

Откройте Pull Request