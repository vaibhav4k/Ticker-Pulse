from flask import Flask, render_template, jsonify, request
from utils import priceFetch

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_price/<symbol>', methods=['GET'])
def get_price(symbol):
    details = priceFetch(symbol)
    return jsonify({
        'symbol': details[0],
        'name': details[1],
        'exchange': details[2],
        'market_price': details[3],
        'price_fetch_time': details[4]
    })

if __name__ == "__main__":
    app.run(debug=True)
 