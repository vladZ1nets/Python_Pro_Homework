from flask import Flask, request

app = Flask(__name__)

'''
 /login [GET, POST]
/register [GET, POST]
/logout [GET ? POST ?? DELETE]

/profile (/user, /me) [GET, PUT(PATCH), DELETE]
      ?  /favouties [GET, POST, DELETE, PATCH]
      ??  /favouties/<favourite_id> [DELETE]
      ?  /search_history [GET, DELETE]

/items [GET, POST]
/items/<item_id> [GET, DELETE]
/leasers [GET]
/leasers/<leaser_id> [GET]

/contracts [GET, POST]
/contracts/<contract_id> [GET, PATCH/PUT]

/search [GET, (POST)]

/complain [POST]
/compare [GET, PUT/PATCH]

 '''
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

@app.route('/logout', methods=['GET', 'POST', 'DELETE'])
def logout():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

@app.route('/items/<item_id>', methods=['GET', 'DELETE'])
def item_detail(item_id):
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass

@app.route('/profile', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
@app.route('/me', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def profile():
    if request.method == 'GET':
        pass
    elif request.method in ['PUT', 'PATCH']:
        pass
    elif request.method == 'DELETE':
        pass

@app.route('/profile/favorites', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def favorites():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PATCH':
        pass

@app.route('/profile/favorites/<favourite_id>', methods=['DELETE'])
def favorite_detail(favourite_id):
    pass

@app.route('/profile/search_history', methods=['GET', 'DELETE'])
def search_history():
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass

@app.route('/leasers', methods=['GET'])
def leasers():
    pass

@app.route('/leasers/<leaser_id>', methods=['GET'])
def leaser_detail(leaser_id):
    pass

@app.route('/contracts', methods=['GET', 'POST'])
def contracts():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

@app.route('/contracts/<contract_id>', methods=['GET', 'PATCH', 'PUT'])
def contract_detail(contract_id):
    if request.method == 'GET':
        pass
    elif request.method in ['PATCH', 'PUT']:
        pass

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

@app.route('/complain', methods=['POST'])
def complain():
    pass

@app.route('/compare', methods=['GET', 'PUT', 'PATCH'])
def compare():
    if request.method == 'GET':
        pass
    elif request.method in ['PUT', 'PATCH']:
        pass

if __name__ == '__main__':
    app.run(debug=True)
