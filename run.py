
from flask import Flask, request, jsonify
from flask_cors import CORS
from bubbleSort import BubbleSort

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "ok"

@app.route('/add_array', methods=['POST'])
def pushdata():
    data = request.get_json()
    func = data['func']
    array=data['array']
    if func == "push":
        newdata=int(data['newdata'])
        array.append(newdata)
    elif func == "clear":
        array = []
    elif func == "delete":
        newdata=int(data['newdata'])
        array.pop(newdata)
    elif func == "sort":
        BubbleSort(array)
    
    return jsonify(array)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)