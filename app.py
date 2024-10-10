from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route('/menu')
def menu():
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h2>Меню (см. ниже)</h2>
        <ul>
            <li><a href="http://127.0.0.1:5000/lab1">Первая лабораторная</a></li>
        </ul>

        <footer>
            &copy; Альбина Кобзева, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
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

@app.route('/lab1/oak')
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

@app.route('/lab1/student')
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


@app.route('/lab1/python')
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

@app.route('/lab1/vk')
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
@app.route('/lab2/a')
def a():
    return 'без слэша'


@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        return 'цветок: ' + flower_list[flower_id]
    
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name}</p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

@app.route('/lab2/example')
def example ():
    name = 'Альбина Кобзева'
    return render_template('example.html', name=name)