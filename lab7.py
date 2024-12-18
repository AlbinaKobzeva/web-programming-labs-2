from flask import Blueprint, render_template, abort, request
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
    return films
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    return films[id] 

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
    films[id] = film
    return films[id] 

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film:
        abort(400)
    films.append(film)
    return film, 201