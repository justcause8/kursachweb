from flask import Flask, render_template

app = Flask(__name__)

nav = [
    { "title": "Главная", "URL": "/" },
    { "title": "Оксфорд", "URL": "/oxford" },
    { "title": "Кембридж", "URL": "/cambridge" },
    { "title": "Имперский колледж Лондона", "URL": "/colledgeLondon" },
    { "title": "Обо мне", "URL": "/about" },
    { "title": "Глоссарий", "URL": "/glossariy" },
]

@app.context_processor
def global_context():
    return{
        "nav": nav
    }

@app.route("/")
def hello_world():
    return render_template("glavnaya.html", name = "Главная" )

@app.route("/oxford")
def cxford_view():
    return render_template("oxford.html", name = "Оксфорд" )

@app.route("/cambridge")
def cambridge_view():
    return render_template("cambridge.html", name = "Кембридж" )

@app.route("/colledgeLondon")
def colledgeLondon_view():
    return render_template("colledgeLondon.html", name = "Имперский колледж Лондона" )

@app.route("/about")
def about_view():
    return render_template("about.html", name = "Обо мне")

@app.route("/glossariy")
def glossariy_view():
    return render_template("glossariy.html", name = "Глоссарий")
