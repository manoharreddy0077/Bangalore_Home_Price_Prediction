from flask import Flask,request,jsonify
import util

app = Flask(__name__)
# @app.route('/hello')
# def hello():
#     return "HI"
# simple basic python server

# our actual routines ==> 2
# first routine is to return the location in bangalore city(locqtion incolumns.json file) in util file return __loactions
#second routine(func) is a fcuntion  to return  estimated price for given bhk ,bath etc etc
# so we create sub dir in server called artifacts
# we store .pickle and columns.json
# now we read columns.json

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-control-Allow-Origin','*')

    return response

# create another end point
# @app.route('/predict_home_price',methods=['POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqft'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])
#
#     response=jsonify({
#         'estimated_price':util.get_estimated_price(location,sqft,bhk,bath)
#     })
#
#     response.headers.add('Access-Control-Allow_origin','*')
#
#     return response



# ... (your other routes)

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)  # Corrected variable name to total_sqft
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()






if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()