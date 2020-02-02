from flask import Flask, render_template, request, redirect, url_for,session,flash
from shopee import scrap_shopee
from lazada import scrap_lazada
from firebase.firebase import FirebaseApplication
from classes import Shopee,Track


app = Flask(__name__)
app.secret_key = "ayush" 
app.config["DEBUG"] = True
url = "https://productify-3f2ab.firebaseio.com/"
firebase = FirebaseApplication(url, None)

def verify_user(username,password): # a function to verify the user's credentials
    result = firebase.get("/users", None)
    for i in result:
        if i == username:
            if result[i]["password"] == password:
                return True
    return False

@app.route('/', methods=['GET', 'POST'])  #homepage
def home():
    try:
        username = session['username']
    except Exception:
        flash("You must log in first!")
        return render_template("index.html") # return to home page if user doesn't login' but he's trying to search products
        
    if request.method == "POST":
        item = request.form['item']
        return redirect('/search/{}'.format(item)) # redirect to the result page
    try:
        return render_template("index.html",username=username) # return to home page with user's username
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
            return redirect(url_for('home')) #direct to home page with user's username
        else:
            flash("You entered an invalid username or password.")
            return render_template("login.html") # prompt user to try again if he entered a wrong username or password
       
    try:
        return render_template("login.html")
    except Exception:
        return render_template("error.html")
    
@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username', None) # clear all the login information
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
    # post the tracking product's informaton to firebase
    result = firebase.post("/{}".format(username),{"name":name,"platform":platform[13:],"product url":p_url,"initial-price":price[6:],"scrape-price":0,"Last-updated":0})
    return "nothing" #i do this because it has to return something

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['pass']
        #store the username and password to the firebase
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
        
        result = scrap_shopee(item,30) # scrape the products from shopee
        
        result += scrap_lazada(item,30) # scrape the products from lazada
       
        return render_template("results.html", products=result,username=username,length=len(result))
    except Exception:
        return render_template("error.html")


@app.route('/track')
def track():
    username = session['username']
    result = firebase.get("/{}".format(username), None)
    if result is None:
        flash("Your tracking list is empty.")
        return render_template("track.html") # show the message when the tracking list is empty
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
    #display all the tracking information in tracking webpage
    return render_template("track.html",products=products,username=username)
            
    
    
if __name__ == "__main__":
    app.run()
