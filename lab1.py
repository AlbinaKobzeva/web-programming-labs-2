from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)

@lab1.route("/lab1")
def lab():
    return '''
<!doctype html>
<html
    <head>
        <title>Кобзева Альбина Алексеевна, лабораторная 1</title>
    </head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
        
        <h2>
            Реализованные роутеры
        </h2>

        <ul>
            <li><a href="http://127.0.0.1:5000/lab1/oak">Дуб</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/student">Студент</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/python">Python</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/vk">VK</a></li>
        </ul>
        <footer>
            &copy; Альбина Кобзева, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@lab1.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''")
    <body>
        <h1 style='padding-left: 15px'>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''" class='oak'>
    </body>
</html>
'''


@lab1.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Кобзева Альбина Алексеевна</h1>
        <img src="''' + url_for('static', filename='nstu.jpeg') + '''" class='nstu'>
    </body>
</html>
'''


@lab1.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Python</h1>
        <p>
            Python — мультипарадигмальный высокоуровневый язык программирования общего назначения с динамической строгой типизацией 
            и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода 
            и его качества, а также на обеспечение переносимости написанных на нём программ.
        </p>
        <p>
            Python разработан Гвидо Ван Россумом (Guido Van Rossum), программистом из Нидерландов. 
            Он начал работу над языком в 1989 году в центре Centrum Wiskunde & Informatica (CWI).
        </p>
        <img src="''' + url_for('static', filename='python.jpg') + '''" class='python'>
    </body>
</html>
'''


@lab1.route('/lab1/vk')
def vk():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>VK</h1>
        <p>
            «ВКонта́кте» (международное название — VK) — российская социальная сеть 
            со штаб-квартирой в Санкт-Петербурге. Запущена в 2006 году Павлом Дуровым.
        </p>
        <p>
            «ВКонтакте» позволяет пользователям отправлять друг другу сообщения, редактировать эти сообщения, 
            создавать собственные страницы и сообщества, обмениваться изображениями, аудио- и видеозаписями, переводить деньги, 
            играть в браузерные игры. Также позиционирует себя платформой для продвижения бизнеса и 
            решения повседневных задач с помощью мини-приложений.
        </p>
        <img src="''' + url_for('static', filename='vk.png') + '''" class='vk'>
    </body>
</html>
'''