from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class DB_local():
    def __init__(self, file_name):
        self.con = sqlite3.connect(file_name)
        self.con.row_factory = dict_factory
        self.cur = self.con.cursor()

    def __enter__(self):
        return self.cur

    def __exit__(self, type, value, traceback):
        self.con.commit()
        self.con.close()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        pass


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        with DB_local('db1.db') as db_cur:
            form_data = request.form
            db_cur.execute('''INSERT INTO user(login, password, full_name, ipn, contacts, photo, passport) 
            VALUES (?, ?, ?, ?, ?, ?, ?)''', (
                form_data['login'], form_data['password'], form_data['full_name'],
                form_data['ipn'], form_data['contacts'], form_data['photo'],
                form_data['passport']
            ))
            return redirect(url_for('login'))


@app.route('/logout', methods=['GET', 'POST', 'DELETE'])
def logout():
    if request.method == 'GET':
        return render_template('logout.html')
    elif request.method in ['POST', 'DELETE']:
        pass


@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        with DB_local('db1.db') as db_cur:
            db_cur.execute("SELECT * FROM items")
            items = db_cur.fetchall()
        return render_template('item.html', items=items)
    elif request.method == 'POST':
        with DB_local('db1.db') as db_cur:
            db_cur.execute('''INSERT INTO items(photo, name, description, price_hour, price_day, price_week, price_month)
            VALUES (:photo, :name, :description, :price_hour, :price_day, :price_week, :price_month)''', request.form)
            return redirect(url_for('items'))


@app.route('/items/<int:item_id>', methods=['GET', 'DELETE'])
def item_detail(item_id):
    if request.method == 'GET':
        with DB_local('db1.db') as db_cur:
            db_cur.execute("SELECT * FROM items WHERE id = ?", (item_id,))
            item = db_cur.fetchone()
        return render_template('item_detail.html', item=item)
    elif request.method == 'DELETE':
        with DB_local('db1.db') as db_cur:
            db_cur.execute("DELETE FROM items WHERE id = ?", (item_id,))
            return redirect(url_for('items'))


@app.route('/profile', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
@app.route('/me', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def profile():
    user_id = id
    if request.method == 'GET':
        with DB_local('db1.db') as db_cur:
            db_cur.execute("SELECT * FROM user WHERE id = ?", (user_id,))
            user = db_cur.fetchone()
        return render_template('profile.html', user=user)
    elif request.method in ['PUT', 'PATCH']:
        pass
    elif request.method == 'DELETE':
        pass


@app.route('/profile/favorites', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def favorites():
    user_id = id
    if request.method == 'GET':
        with DB_local('db1.db') as db_cur:
            db_cur.execute("SELECT * FROM favorites WHERE user_id = ?", (user_id,))
            favorites = db_cur.fetchall()
        return render_template('favorites.html', favorites=favorites)
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PATCH':
        pass


@app.route('/profile/favorites/<int:favourite_id>', methods=['DELETE'])
def favorite_detail(favourite_id):
    pass


@app.route('/profile/search_history', methods=['GET', 'DELETE'])
def search_history():
    user_id = id  # Приклад замісника
    if request.method == 'GET':
        with DB_local('db1.db') as db_cur:
            db_cur.execute("SELECT * FROM search_history WHERE user_id = ?", (user_id,))
            history = db_cur.fetchall()
        return render_template('search_history.html', history=history)
    elif request.method == 'DELETE':
        pass


@app.route('/leasers', methods=['GET'])
def leasers():
    with DB_local('db1.db') as db_cur:
        db_cur.execute("SELECT * FROM leasers")
        leasers = db_cur.fetchall()
    return render_template('leasers.html', leasers=leasers)


@app.route('/leasers/<int:leaser_id>', methods=['GET'])
def leaser_detail(leaser_id):
    with DB_local('db1.db') as db_cur:
        db_cur.execute("SELECT * FROM leasers WHERE id = ?", (leaser_id,))
        leaser = db_cur.fetchone()
    return render_template('leaser_detail.html', leaser=leaser)


@app.route('/contracts', methods=['GET', 'POST'])
def contracts():
    if request.method == 'GET':
        with DB_local('db1.db') as db_cur:
            db_cur.execute("SELECT * FROM contracts")
            contracts = db_cur.fetchall()
        return render_template('contracts.html', contracts=contracts)
    elif request.method == 'POST':
        pass


@app.route('/contracts/<int:contract_id>', methods=['GET', 'PATCH', 'PUT'])
def contract_detail(contract_id):
    if request.method == 'GET':
        with DB_local('db1.db') as db_cur:
            db_cur.execute("SELECT * FROM contracts WHERE id = ?", (contract_id,))
            contract = db_cur.fetchone()
        return render_template('contract_detail.html', contract=contract)
    elif request.method in ['PATCH', 'PUT']:
        pass


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    elif request.method == 'POST':
        search_query = request.form['query']
        with DB_local('db1.db') as db_cur:
            db_cur.execute("SELECT * FROM items WHERE name LIKE ?", ('%' + search_query + '%',))
            results = db_cur.fetchall()
        return render_template('search_results.html', results=results)


@app.route('/complain', methods=['POST'])
def complain():
    pass


@app.route('/compare', methods=['GET', 'PUT', 'PATCH'])
def compare():
    if request.method == 'GET':
        return render_template('compare.html')
    elif request.method in ['PUT', 'PATCH']:
        pass


if __name__ == '__main__':
    app.run(debug=True)
