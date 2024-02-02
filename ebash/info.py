ROUT_INFO = [
    {
        "endpoint": "/",
        "method" : "GET",
        "required": "none",
        "description": "список всех роутов",
        "auth": "none"
    },
    {
        "endpoint": "login/",
        "method" : "POST",
        "required": "username(str), password(str)",
        "description": "логинимся тут",
        "auth": "none"
    },
    {
        "endpoint": "signup/",
        "method" : "POST",
        "required": "username(str), password(str), email(str)",
        "description": "регаемся тут",
        "auth": "none"
    },
    {
        "endpoint": "logout/",
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
        "required": "name(str), body(str)",
        "description": "создание скрипта",
        "auth": "обязательно"
    },
    {
        "endpoint": "scripts/<id>/update/",
        "method" : "PUT",
        "required": "name(str), body(str), color(str)",
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
]