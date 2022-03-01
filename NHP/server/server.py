import os
os.environ['PATH']
from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_house_price',methods = ['GET','POST'])
def predict_house_price():
    Region = request.form['Region']
    Bedrooms = int(request.form['Bedrooms'])
    Bathrooms = int(request.form['Bathrooms'])
    total_sqft = float(request.form['total_sqft'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(Region,Bedrooms,Bathrooms,total_sqft)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Hor Price Prediction....")
    app.run()