from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Кобзева Альбина Алексеевна, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h>

        <footer>
            &copy; Альбина Кобзева, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""