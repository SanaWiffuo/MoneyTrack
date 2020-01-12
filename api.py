from flask import Flask, render_template, request, redirect, url_for
from shopee import scrap_shopee
from lazada import scrap_lazada
from threading import Thread
import queue

app = Flask(__name__)
app.config["DEBUG"] = True
l_queue = queue.Queue()
s_queue = queue.Queue()
over = queue.Queue()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        item = request.form['item']
        num = request.form['num']
        return redirect('/search/{}/{}'.format(item, num))
    return render_template("index.html")


@app.route('/search/<string:item>/<int:num>', methods=['GET'])
def search(item, num):
    try:
        l = Thread(target=scrap_lazada ,args=(item,num, l_queue,over))
        l.start()
        s = Thread(target=scrap_shopee,args=(item, num, s_queue,over))
        s.start()
        
        result = over.get()
        s.join()
        l.join()
        result += over.get()

        return render_template("results.html", products=result)
    except Exception:
        return render_template("error.html")


app.run()
