# -*- coding: UTF-8 -*-
from app import app


@app.route('/')
def index():
    return 'Flask API start'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)