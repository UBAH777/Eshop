# EShop - shop of gadgets
Представляем Вашему вниманию магазин электрониики и техники

### Технологии

- `python3.9`
- пакеты python из файла requirements.txt
- инструменты `make`
- `redis`
- `docker`

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
├──Volume/
    └── db.sqlite3
├── run.sh
├── manage.py
└── celerybeat-schedule.db
```

### Подготовка и запуск

#### Установка

- установить `python` в вашей ОС
- установить `make` в вашей ОС
- установить `redis` в вашей ОС
- склонировать репозиторий

#### Запуск при помощи Make

- При первом запуске (для настройки проекта и запуска): запустить `make up_service`; при последующих запусках: `make run`.
- Параллельно этому в отдельном процессе выполнить (под виртуальным окружением) `celery -A Eshop beat -l info`
- Также должен быть отдельно запущен сервис `redis` на `6379` порте. (Например, с помощью `sudo systemctl start redis`, если `redis` скачан, но не запущен)
