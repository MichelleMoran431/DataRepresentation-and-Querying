from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

#get all
@app.route('/coffeeconsumers')
def getAll():
    return jsonify([])

# find By id
@app.route('/coffeeconsumers/<int:id>')
def findById(id):
    return jsonify({}) 

# create
# curl -X POST -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books

@app.route('/coffeeconsumers', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    
    coffeeconsumer = {
        "id": request.json["id"],,
        "firstname": request.json["firstname"],
        "lastname": request.json["lastname"],
        "postcode": request.json["postcode"]
    }
    return jsonify({})


    return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/coffeeconsumers/<int:id>', methods=['PUT'])
def update(id):
    if len(foundBooks) == 0:
        return jsonify({}), 404
    currentBook = foundBooks[0]
    if 'firstname' in request.json:
        currentBook['firstname'] = request.json['firstname']
    if 'lastname' in request.json:
        currentBook['lastname'] = request.json['lastname']
    if 'postcode' in request.json:
        currentBook['postcode'] = request.json['postcode']

    return jsonify(currentBook)

#delete
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/coffeeconsumers/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)
