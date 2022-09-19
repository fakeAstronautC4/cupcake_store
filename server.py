from threading import local
from flask import Flask, render_template, redirect, url_for
from cupcakes import reader, find_cupcake, add_to_order
import csv


app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000
def index():
    return render_template('index.html')  # <<----------- REQUIRED RETURN STATEMENT UNDER @APP.ROUTE

@app.route('/cupcakes')
def cupcakes():
    return render_template('cupcakes.html', cupcakes = reader('cupcake_list.csv'))

@app.route('/cupcake/<flavor>')
def cupcake(flavor):
    new_cupcake = find_cupcake(flavor)
    
    if new_cupcake:
        add_to_order(new_cupcake)
        return redirect(url_for('index'))
    else:
        return "Sorry, 404 on that cupcake"
    
    

@app.route('/order')
def order():    
    return render_template('order.html')


if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000)