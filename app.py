from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

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
            <li><a href="http://127.0.0.1:5000/lab2">Вторая лабораторная</a></li>
        </ul>

        <footer>
            &copy; Альбина Кобзева, ФБИ-24, 3 курс, 2024
        </footer>
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