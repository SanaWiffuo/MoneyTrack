from flask import Flask, render_template, request, redirect, url_for,session,flash
from shopee import scrap_shopee
from lazada import scrape
from firebase.firebase import FirebaseApplication
from classes import Shopee,Track


app = Flask(__name__)
app.secret_key = "ayush" 
app.config["DEBUG"] = True
url = "https://productify-3f2ab.firebaseio.com/"
firebase = FirebaseApplication(url, None)

def verify_user(username,password):
    result = firebase.get("/users", None)
    for i in result:
        if i == username:
            if result[i]["password"] == password:
                return True
    return False

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        username = session['username']
    except Exception:
        flash("You must log in first!")
        return render_template("index.html") 
        
    if request.method == "POST":
        item = request.form['item']
        return redirect('/search/{}'.format(item))
    try:
        return render_template("index.html",username=username)
    except Exception:
        return render_template("error.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['pass']
        if verify_user(username, password):
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash("You entered an invalid username or password.")
            return render_template("login.html")
       
    try:
        return render_template("login.html")
    except Exception:
        return render_template("error.html")
    
@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username', None) 
    try:
        return redirect(url_for('home'))
    except Exception:
        return render_template("error.html")

@app.route('/generate')
def generate():
    name = request.args['name']
    platform = request.args['platform']
    p_url = request.args['link']
    price = request.args['price']
    username = request.args['username']
    result = firebase.post("/{}".format(username),{"name":name,"platform":platform[13:],"product url":p_url,"initial-price":price[6:],"scrape-price":0,"Last-updated":0})
    return "nothing" #i do this because it has to return something

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['pass']
        result = firebase.put("/users",username,{"password":password})
        return render_template("index.html")
    try:
        return render_template("signup.html")
    except Exception:
        return render_template("error.html")


@app.route('/search/<string:item>', methods=['GET'])
def search(item):
    try:
        username = session['username']
        # result = [Shopee("ex","100",5.0,"https://shopee.sg/Anmite-24-75Hz-IPS-Curved-FHD-LED-Monitor-Hdmi-HDR-Super-Slim-and-Sleek-Design-i.152295628.2285979907","https://cf.shopee.sg/file/b83e20398e1991117b95ba9c81bd8a3d"),Shopee("ch","50",5.0,"https://shopee.sg/Anmite-24-75Hz-IPS-Curved-FHD-LED-Monitor-Hdmi-HDR-Super-Slim-and-Sleek-Design-i.152295628.2285979907","https://cf.shopee.sg/file/b83e20398e1991117b95ba9c81bd8a3d")]
        result = scrap_shopee(item,30)
        # try:
        #     result += scrape(item,30)
        # except IndexError:
        #     pass


        return render_template("results.html", products=result,username=username,length=len(result))
    except Exception:
        return render_template("error.html")


@app.route('/track')
def track():
    username = session['username']
    result = firebase.get("/{}".format(username), None)
    if result is None:
        flash("Your tracking list is empty.")
        return render_template("track.html")
    products = []
    for key in result:
        p = result[key]
        last_updated = p['Last-updated']
        initial_price = p['initial-price']
        name = p['name']
        platform = p['platform']
        url = p['product url']
        scrape_price = p['scrape-price']
        products.append(Track(name,initial_price,scrape_price,url,last_updated,platform))

    return render_template("track.html",products=products,username=username)
            
    
    
if __name__ == "__main__":
    app.run()
