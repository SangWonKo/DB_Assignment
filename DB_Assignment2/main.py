from flask import Flask, render_template, request
from flask_cors import CORS
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', template_folder='../templates')

@app.route('/insertC', methods=['GET', 'POST'])
def insert():

    db = pymysql.connect(
        user='root',
        passwd='kosang9487',
        host='localhost',
        db='db_assignment',
        charset='utf8'
    )

    if request.method == 'POST':
        customer_info = request.form

        name = customer_info['name']
        phone = customer_info['phone']
        address = customer_info['address']
        gender = customer_info['gender']

    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = "INSERT INTO customer(name, phone, address, gender) VALUES('%s', '%s', '%s', '%s')" % (name, phone, address, gender)
    cursor.execute(query)

    db.commit()

    return render_template('index.html')

@app.route('/insertT', methods=['GET', 'POST'])
def insertT():
    db = pymysql.connect(
        user='root',
        passwd='kosang9487',
        host='localhost',
        db='db_assignment',
        charset='utf8'
    )

    if request.method == 'POST':
        transaction_info = request.form

        tNumber = transaction_info['tNumber']
        productID = transaction_info['productID']
        price = transaction_info['price']
        date = transaction_info['date']
        customerName = transaction_info['customerName']

    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = "INSERT INTO transaction VALUES('%s', '%s', '%s', '%s', '%s')" % (tNumber, productID, price, date, customerName)
    cursor.execute(query)

    db.commit()

    return render_template('index.html')

@app.route('/insertP', methods=['GET', 'POST'])
def insertP():

    db = pymysql.connect(
        user='root',
        passwd='kosang9487',
        host='localhost',
        db='db_assignment',
        charset='utf8'
    )

    if request.method == 'POST':
        transaction_info = request.form

        name = transaction_info['name']
        productID = transaction_info['productID']
        supplierName = transaction_info['supplierName']
        

    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = "INSERT INTO transaction VALUES('%s', '%s', '%s')" % (name, productID, supplierName)
    cursor.execute(query)

    db.commit()

    return render_template('index.html')

@app.route('/select')
def select():
    return render_template('select.html')

@app.route('/select/customer')
def selectC():
    
    return render_template('select.html')

@app.route('/select/transaction')
def selectT(foo):
    return render_template('select.html')

@app.route('/select/product')
def selectP(foo):
    return render_template('select.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)