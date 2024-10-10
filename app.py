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

all_flower_list = [
    {'name': 'роза', 'kolvo': 5},
    {'name': 'тюльпан', 'kolvo': 15},
    {'name': 'гипсофила', 'kolvo': 10},
    {'name': 'ромашка', 'kolvo': 20},
]

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(all_flower_list):
        return "Такого цветка нет", 404
    else:
        return render_template('addflower.html', flower_id=flower_id, flower=all_flower_list[flower_id])
    
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    for flower in all_flower_list:
        if flower['name'] == name:
            return f"Цветок с именем {name} уже существует.", 400
    all_flower_list.append({'name': name, 'kolvo': 1})  
    return redirect(url_for('all_flowers'))
@app.route('/lab2/flower/')
def no_flower():
    return "Вы не задали имя цветка", 400   
@app.route('/lab2/all_flowers')
def all_flowers():
    return render_template('flowers.html', all_flower_list=all_flower_list)
@app.route('/lab2/flowers/clear')
def clear_flowers():
    all_flower_list.clear()
    return redirect(url_for('all_flowers'))

@app.route('/lab2/example')
def example ():
    name = 'Альбина Кобзева'
    numberLab = '2'
    groupStudent = 'ФБИ-24'
    numberCourse = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html', name=name, numberLab=numberLab,
                           groupStudent=groupStudent, numberCourse=numberCourse, 
                           fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return render_template('calc.html', a=a, b=b)
@app.route('/lab2/calc/')
def calc_without_numbers():
    return redirect(url_for('calc', a=1, b=1))
@app.route('/lab2/calc/<int:a>/')
def calc_with_a(a):
    return redirect(url_for('calc', a=a, b=1))

book_list = [
    {"author": "Хьюберт Селби", "name": "Реквием по мечте", "genre": "Психологический-реализм", "pages": 320},
    {"author": "Филип Пулман", "name": "Тень горы", "genre": "Фэнтези", "pages": 464},
    {"author": "Дэниел Киз", "name": "Цветы для Элджернона", "genre": "Научная фантастика", "pages": 311},
    {"author": "Джордж Оруэлл", "name": "Скотный двор", "genre": "Сатира", "pages": 112},
    {"author": "Габриэль Гарсиа Маркес", "name": "Любовь во время холеры", "genre": "Роман", "pages": 368},
    {"author": "Артур Конан Дойл", "name": "Приключения Шерлока Холмса", "genre": "Детектив", "pages": 307},
    {"author": "Джером Д. Сэлинджер", "name": "Над пропастью во ржи", "genre": "Роман", "pages": 277},
    {"author": "Джон Стейнбек", "name": "Гроздья гнева", "genre": "Роман", "pages": 464},
    {"author": "Роберт Гэлбрейт", "name": "Крестный отец", "genre": "Криминальный роман", "pages": 448},
    {"author": "Эмили Бронте", "name": "Грозовой перевал", "genre": "Роман", "pages": 416},
    {"author": "Джейн Остин", "name": "Эмма", "genre": "Роман", "pages": 474},
]

@app.route('/lab2/books')
def books():
    return render_template('books.html', book_list=book_list)

objects = [
    {
        "name": "Джордан",
        "image": "джордан.jpg"
    },
    {
        "name": "лакост",
        "image": "лакост.jpg"
    },
    {
        "name": "баленсиага",
        "image": "баленсиага.jpg"
    },
    {
        "name": "осирис",
        "image": "осирис.jpg"
    },
    {
        "name": "рики",
        "image": "рики.jpg"
    }
]
@app.route('/lab2/spisok')
def spisok():
    return render_template('spisok.html', objects=objects)