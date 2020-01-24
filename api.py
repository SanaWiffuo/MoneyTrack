from flask import Flask, render_template, request, redirect, url_for
from shopee import scrap_shopee
from lazada import scrap_lazada
from threading import Thread
import queue
from firebase.firebase import FirebaseApplication

app = Flask(__name__)
app.config["DEBUG"] = True
l_queue = queue.Queue()
s_queue = queue.Queue()
over = queue.Queue()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        item = request.form['item']
        return redirect('/search/{}'.format(item))
    try:
        return render_template("index.html")
    except Exception:
        return render_template("error.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']
        return redirect('/')
    try:
        return render_template("login.html")
    except Exception:
        return render_template("error.html")

@app.route('/generate')
def generate():
    name = request.args['name']
    platform = request.args['platform']
    p_url = request.args['link']
    price = request.args['price']
    url = "https://productify-3f2ab.firebaseio.com/"  
    firebase = FirebaseApplication(url, None)
    result = firebase.post("/zachary",{"name":name,"platform":platform,"product url":p_url,"initial-price":price,"scrape-price":0})
    return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']
        return redirect('/')
    try:
        return render_template("signup.html")
    except Exception:
        return render_template("error.html")


@app.route('/search/<string:item>', methods=['GET'])
def search(item):
    try:
        # result = [Shopee("monitor",100,5.0,"https://shopee.sg/Anmite-24-75Hz-IPS-Curved-FHD-LED-Monitor-Hdmi-HDR-Super-Slim-and-Sleek-Design-i.152295628.2285979907","https://cf.shopee.sg/file/b83e20398e1991117b95ba9c81bd8a3d"),Shopee("monitor",100,5.0,"https://shopee.sg/Anmite-24-75Hz-IPS-Curved-FHD-LED-Monitor-Hdmi-HDR-Super-Slim-and-Sleek-Design-i.152295628.2285979907","https://cf.shopee.sg/file/b83e20398e1991117b95ba9c81bd8a3d")]
        l = Thread(target=scrap_lazada, args=(item, 10, l_queue, over))
        l.start()
        s = Thread(target=scrap_shopee, args=(item, 10, s_queue, over))
        s.start()

        result = over.get()
        s.join()
        l.join()
        result += over.get()
        print(result)
        return render_template("results.html", products=result)
    except Exception:
        return render_template("error.html")


# @app.route('/track', methods=['GET', 'POST'])
# def track():
#     if request.method == "POST":


app.run()
