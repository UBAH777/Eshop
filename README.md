# EShop - shop of gadgets
Представляем Вашему вниманию магазин электрониики и техники

### Технологии

- python
- пакеты python из файла requirements.txt
- инструменты make

### Структура

```shell
.
├── Eshop/
│   ├── asgi.py
│   ├── celery.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── contact/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations/
│   ├── models.py
│   ├── service.py
│   ├── tasks.py
│   ├── templatetags/
│   │   ├── contact_tags.py
│   │   ├── __init__.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── shop/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations/
│   ├── models.py
│   ├── templatetags/
│   │   ├── __init__.py
│   │   ├── item_tag.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media/
│   ├── item_images/
│   ├── item_shots/
│   └── vendor_icons/
├── static/
│   ├── admin/
│   │   ├── css/
│   │   ├── fonts/
│   │   ├── img/
│   │   └── js/
│   ├── ckeditor/
│   ├── css/
│   ├── img/
└── templates/
    ├── account/
    ├── base.html/
    ├── contact/
    ├── include/
    ├── pages/
    └── shop/
├── run.sh
├── db.sqlite3
├── manage.py
├── celerybeat-schedule.db
```

### Подготовка и запуск

#### Установка

- установить python в вашей ОС
- установить make в вашей ОС
- склонировать репозиторий

#### Запуск

- при первом запуске (для настройки проекта и запуска): запустить `make launch`
- при последующих запусках: `make run`

### Дополнительно

- при развертывании на удаленной машине используйте `docker`
