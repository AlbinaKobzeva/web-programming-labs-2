from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response (redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response (redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors={}
    user = request.args.get('user')
    if user == '':
        errors['user']= 'Заполните поле!'
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
        return render_template('lab3/order.html')
@lab3.route('/lab3/pay')
def pay():
        price=0
        drink = request.args.get('drink')
        #Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый - 70 рублей.
        if drink == 'coffee':
             price= 120
        elif drink == 'black-tea':
             price = 80
        else:
             price=70
        #Добавка молодка удорожает напиток на 30 рублей, а сахар - на 10.
        if request.args.get('milk') == 'on':
             price += 30
        if request.args.get('sugar') == 'on':
             price += 10
        return render_template('lab3/pay.html', price=price)
@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')
    return render_template('lab3/success.html', price=price)

@lab3.route('/lab3/settings')
def settings():
    # Получаем параметры из запроса
    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    font_style = request.args.get('font_style')
    # Если параметры переданы, сохраняем их в cookies
    if color or bg_color or font_size or font_style:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if bg_color:
            resp.set_cookie('bg_color', bg_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if font_style:
            resp.set_cookie('font_style', font_style)
        return resp
    else:
        # Загружаем параметры из cookies
        color = request.cookies.get('color', '#ffffff')
        bg_color = request.cookies.get('bg_color', '#000000')
        font_size = request.cookies.get('font_size', '15')
        font_style = request.cookies.get('font_style', 'normal')
        resp = make_response(render_template('lab3/settings.html', 
                                             color=color, 
                                             bg_color=bg_color, 
                                             font_size=font_size, 
                                             font_style=font_style))
        return resp
    

@lab3.route('/lab3/ticket')
def ticket():
    passenger_name = request.args.get('passenger_name')
    shelf_type = request.args.get('shelf_type')
    with_bedding = request.args.get('with_bedding')
    with_luggage = request.args.get('with_luggage')
    age = request.args.get('age')
    departure_point = request.args.get('departure_point')
    destination_point = request.args.get('destination_point')
    travel_date = request.args.get('travel_date')
    insurance_needed = request.args.get('insurance_needed')
    if passenger_name and shelf_type and age and departure_point and destination_point and travel_date:
        age = int(age)
        
        ticket_price = 1000 if age >= 18 else 700  
        if shelf_type in ['lower', 'lower_side']:
            ticket_price += 100
        if with_bedding == 'on':
            ticket_price += 75
        if with_luggage == 'on':
            ticket_price += 250
        if insurance_needed == 'on':
            ticket_price += 150
        ticket_type = "Детский билет" if age < 18 else "Взрослый билет"
        return render_template('lab3/train.html', 
                               passenger_name=passenger_name, 
                               ticket_type=ticket_type,
                               ticket_price=ticket_price,
                               departure_point=departure_point,
                               destination_point=destination_point,
                               travel_date=travel_date)
    return render_template('lab3/ticket.html')


@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    resp = make_response(redirect('/lab3/settings'))
    
    # Удаляем все куки
    resp.delete_cookie('color')
    resp.delete_cookie('bg_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('font_style')
    
    return resp


products = [
    {"name": "iPhone 14", "price": 75500, "color": "pink", "brand": "Apple"},
    {"name": "iPhone13", "price": 60000, "color": "black", "brand": "Apple"},
    {"name": "iPhone16", "price": 159000, "color": "white", "brand": "Apple"},
    {"name": "iPhone15 ProMax", "price": 100000, "color": "platinum", "brand": "Apple"},
    {"name": "iPhone12", "price": 55000, "color": "purple", "brand": "Apple"},
    {"name": "iPhone11", "price": 40000, "color": "black", "brand": "Apple"},
    {"name": "iPhone12 ProMax", "price": 59900, "color": "green", "brand": "Apple"},
    {"name": "iPhone10", "price": 35000, "color": "red", "brand": "Apple"},
    {"name": "iPhone14 ProMax", "price": 130990, "color": "purple", "brand": "Apple"},
    {"name": "iPhone12 mini", "price": 57490, "color": "black", "brand": "Apple"},
    {"name": "MacBook Air", "price": 145900, "color": "silver", "brand": "Apple"},
    {"name": "MacBook Pro", "price": 228900, "color": "grey", "brand": "Apple"},
    {"name": "iPhone16 ProMax", "price": 204900, "color": "white", "brand": "Apple"},
    {"name": "AirPods Pro", "price": 25990, "color": "white", "brand": "Apple"},
    {"name": "AirPods", "price": 25900, "color": "white", "brand": "Apple"},
    {"name": "Apple Watch Series 8", "price": 35890, "color": "silver", "brand": "Apple"},
    {"name": "Apple Watch Series 9", "price": 47800, "color": "black", "brand": "Apple"},
    {"name": "iPhone13 ProMax", "price": 74990, "color": "blue", "brand": "Apple"},
    {"name": "iPad", "price": 48400, "color": "grey", "brand": "Apple"},
    {"name": "iMac", "price": 129990, "color": "green", "brand": "Apple"},
    {"name": "AirPods Max", "price": 50990, "color": "pink", "brand": "Apple"}
]


@lab3.route('/lab3/form')
def form():
    return render_template('lab3/form.html')
@lab3.route('/lab3/results')
def results():
    min_price = request.args.get('min_price', type=int)
    max_price = request.args.get('max_price', type=int)
    filtered_products = [p for p in products if min_price <= p["price"] <= max_price]
    return render_template('lab3/results.html', products=filtered_products)