from flask import Blueprint, render_template, abort, request, jsonify
from datetime import datetime
lab7 = Blueprint('lab7', __name__)
@lab7.route('/lab7/')
def lab():
    return render_template('lab7/lab7.html')
films = [
    {
        "title": "The Age of Adaline",
        "title_ru": "Век Адалин",
        "year": 2015,
        "description": "Вечно молодая Адалин встречает мужчину, ради которого готова состариться. Фантастическая драма с Блейк Лайвли."
    },
    {
        "title": "A Man Called Ove",
        "title_ru": "Вторая жизнь Уве",
        "year": 2015,
        "description": "Сварливый вдовец-придира находит смысл жизни с появлением новых соседей. Добрый фильм по шведскому бестселлеру."
    },
    {
        "title": "Whiplash",
        "title_ru": "Одержимость",
        "year": 2014,
        "description": "Юный барабанщик на тернистом пути к величию. Остросюжетная драма Дэмьена Шазелла, отмеченная тремя «Оскарами»."
    },
    {
        "title": "Love Actually",
        "title_ru": "Реальная любовь",
        "year": 2003,
        "description": "Калейдоскоп смешных и трогательных историй о любви. Фильм, без которого уже нельзя представить себе Рождество."
    },
    {
        "title": "Atonement",
        "title_ru": "Искупление",
        "year": 2007,
        "description": "Семейная трагедия и Вторая мировая война разлучают влюбленных. Щемящая драма о предательстве и покаянии." 
    }
]
@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    return jsonify(films[id]) 

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    del films[id]
    return '', 204 

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    film = request.get_json() 
    if film.get('description', '') == '':
        return jsonify({'description': 'Заполните описание'}), 400
    elif len(film['description']) > 2000:
        return jsonify({'description': 'Описание не должно превышать 2000 символов'}), 400
    if not film.get('title') and not film.get('title_ru'):
        return jsonify({'title': 'Заполните поля с названиями'}), 400
    if not film.get('title_ru'):
        return jsonify({'title_ru': 'Заполните русское название'}), 400
    if film.get('title', '') == '':
        film['title'] = film['title_ru']
    if not film.get('year'):
        return jsonify({'year': 'Укажите год выпуска фильма'}), 400
    elif not str(film['year']).isdigit() or int(film['year']) < 1895 or int(film['year']) > 2100:
        return jsonify({'year': 'Введите корректный год (1800-2100)'}), 400
        
    films[id] = film
    return jsonify(films[id]) 

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film:
        abort(400)
    if film.get('description', '') == '':
        return jsonify({'description': 'Заполните описание'}), 400 
    elif len(film['description']) > 2000:
        return jsonify({'description': 'Описание не должно превышать 2000 символов'}), 400
    if not film.get('title') and not film.get('title_ru'):
        return jsonify({'title': 'Заполните поля с названиями'}), 400
    if not film.get('title_ru'):
        return jsonify({'title_ru': 'Заполните русское название'}), 400
    if film.get('title', '') == '':
        film['title'] = film['title_ru'] 
    if not film.get('year'):
        return jsonify({'year': 'Укажите год выпуска фильма'}), 400
    elif not str(film['year']).isdigit() or int(film['year']) < 1895 or int(film['year']) > 2100:
        return jsonify({'year': 'Введите корректный год (1800-2100)'}), 400
    films.append(film)
    return jsonify(film), 201