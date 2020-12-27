from flask import Flask, render_template, request
from flask_cors import CORS
import pymysql, csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', template_folder='../templates')

@app.route('/insertC', methods=['GET', 'POST'])
def insert():

    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='54.180.147.13',
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
        passwd='1234',
        host='54.180.147.13',
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
        passwd='1234',
        host='54.180.147.13',
        db='db_assignment',
        charset='utf8'
    )

    if request.method == 'POST':
        transaction_info = request.form

        name = transaction_info['name']
        productID = transaction_info['productID']
        supplierName = transaction_info['supplierName']
        

    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = "INSERT INTO product VALUES('%s', '%s', '%s')" % (name, productID, supplierName)
    cursor.execute(query)

    db.commit()

    return render_template('index.html')

@app.route('/select')
def select():
     
    return render_template('select.html')
    

@app.route('/select/customer', methods=['GET', 'POST'])
def selectC():
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='54.180.147.13',
        db='db_assignment',
        charset='utf8'
    )

    if request.method == 'POST':
        customer_info = request.form
        select = customer_info['select']
        
    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = "SELECT %s FROM customer" % (select)
    cursor.execute(query)

    row = cursor.fetchall()
       
    

    return render_template('selectCustomer.html', result = row)

@app.route('/select/transaction', methods=['GET', 'POST'])
def selectT():
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='54.180.147.13',
        db='db_assignment',
        charset='utf8'
    )

    if request.method == 'POST':
        transaction_info = request.form
        select = transaction_info['select']
        
    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = "SELECT %s FROM transaction" % (select)
    cursor.execute(query)

    row = cursor.fetchall()
    print(row)
    return render_template('selectTransaction.html', result = row)

@app.route('/select/product', methods=['GET', 'POST'])
def selectP():
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='54.180.147.13',
        db='db_assignment',
        charset='utf8'
    )

    if request.method == 'POST':
        product_info = request.form
        select = product_info['select']
        
    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = "SELECT %s FROM product" % (select)
    cursor.execute(query)

    row = cursor.fetchall()
       
    

    return render_template('selectProduct.html', result = row)

@app.route('/csv')
def readcsv():
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='54.180.147.13',
        db='db_assignment',
        charset='utf8'
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)

    csv_data = csv.reader(open('data.csv'))
    for row in csv_data:
        if row[0] == "C":
            query = "INSERT INTO customer(name, phone, address, gender) VALUES('%s', '%s', '%s', '%s')" % (row[1], row[2], row[3], row[4])
            cursor.execute(query)
            print(row)
        if row[0] == "T":
            query = "INSERT INTO transaction VALUES('%s', '%s', '%s', '%s', '%s')" % (row[1], row[2], row[3], row[4], row[5])
            cursor.execute(query)
            print(row)
        if row[0] == "P":
            query = "INSERT INTO product VALUES('%s', '%s', '%s')" % (row[1], row[2], row[3]) 
            cursor.execute(query)
            print(row)


    db.commit()
    

    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/search/a')
def a():
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='54.180.147.13',
        db='db_assignment',
        charset='utf8'
    )
        
    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = "SELECT distinct product.name FROM customer, transaction, product \
        WHERE customer.name = transaction.customerName \
        AND transaction.productID = product.productID \
        AND customer.gender='Male' > customer.gender='Female'"
    cursor.execute(query)

    row = cursor.fetchall()
    print(row)

    return render_template('searchA.html', result = row)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='54.180.147.13',
        db='db_assignment',
        charset='utf8'
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        table_info = request.form
        table = table_info['table']

    query = "TRUNCATE %s" % (table)
    cursor.execute(query)

    db.commit()

    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)