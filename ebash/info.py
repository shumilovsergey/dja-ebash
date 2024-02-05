ROUT_INFO = [
    {
        "endpoint": "/",
        "method" : "GET",
        "required": "none",
        "description": "список всех роутов",
        "auth": "none"
    },
    {
        "endpoint": "tg_login",
        "method" : "GET",
        "required": "none",
        "description": "Отдает ссылку для ауторизации через телегу",
        "auth": "none"
    },
    {
        "endpoint": "tg_logout",
        "method" : "GET",
        "required": "none",
        "description": "отрицательно логинимся тут",
        "auth": "обязательно"
    },
    {
        "endpoint": "scripts/",
        "method" : "GET",
        "required": "none",
        "description": "вывод всех скриптов пользователя",
        "auth": "обязательно"
    },
    {
        "endpoint": "scripts/<id>/",
        "method" : "GET",
        "required": "none",
        "description": "вывод скрипта <id>",
        "auth": "none"
    },
    {
        "endpoint": "scripts/create/",
        "method" : "POST",
        "required": "name(str), body(str) | не обязательное поле - color(int)",
        "description": "не обязательный параметр - цвет. можно предложить на выбор из списка /profile/available_colors",
        "auth": "обязательно"
    },
    {
        "endpoint": "scripts/<id>/update/",
        "method" : "PUT",
        "required": "name(str), body(str) | не обязательное поле - color(int)",
        "description": "редактирование скрипта <id>",
        "auth": "обязательно"
    },
    {
        "endpoint": "scripts/<id>/delete/",
        "method" : "DELETE",
        "required": "none",
        "description": "удаление скрипта <id>",
        "auth": "обязательно"
    },
    {
        "endpoint": "scripts/<id>/raw/",
        "method" : "GET",
        "required": "none",
        "description": "вывод RAW скрипта <id>",
        "auth": "none"
    },
    {
        "endpoint": "templates/",
        "method" : "GET",
        "required": "none",
        "description": "вывод всех шаблонов пользователя",
        "auth": "обязательно"
    },
    {
        "endpoint": "templates/<id>/",
        "method" : "GET",
        "required": "none",
        "description": "вывод шаблона <id>",
        "auth": "none"
    },
    {
        "endpoint": "templates/create/",
        "method" : "POST",
        "required": "name(str), body(json)",
        "description": "создание шаблона. структура json. ключ (str) - порядковый номер выполнения, значение (str) - id скрипта",
        "auth": "обязательно"
    },
    {
        "endpoint": "templates/<id>/update/",
        "method" : "PUT",
        "required": "name(str), body(json)",
        "description": "редактирование шаблона <id>. структура json. ключ (str) - порядковый номер выполнения, значение (str) - id скрипта",
        "auth": "обязательно"
    },
    {
        "endpoint": "templates/<id>/delete/",
        "method" : "DELETE",
        "required": "none",
        "description": "удаление шаблона <id>",
        "auth": "обязательно"
    },
    {
        "endpoint": "templates/<id>/raw/",
        "method" : "GET",
        "required": "none",
        "description": "вывод RAW шаблона <id>",
        "auth": "none"
    },   
    {
        "endpoint": "templates/<id>/raw/",
        "method" : "GET",
        "required": "none",
        "description": "вывод RAW шаблона <id>",
        "auth": "none"
    },
    {
        "endpoint": "/profile/available_colors",
        "method" : "GET",
        "required": "none",
        "description": "список пользовательских цветов",
        "auth": "none"
    },
    {
        "endpoint": "/profile/available_avatars",
        "method" : "GET",
        "required": "none",
        "description": "список пользовательских аватаров",
        "auth": "none"
    },
    {
        "endpoint": "/profile/update",
        "method" : "POST",
        "required": "не обязательные поля profile_name (str), color(int), avatar(int)",
        "description": "есть необязательные поля - color и avatar. список доступного содержимого для этих полей можно получить ендпоинтами выше",
        "auth": " обязательно"
    }
]