# Import flask framework
from flask import *

# Below we create a web server based application
app = Flask(__name__)

# Below we create the home route.
# Routing is mapping/connecting different resources to different to different functions. We do this by the help of a decorator.
@app.route("/api/home")
def home():
    return jsonify({"message" : "Home Route Accessed"})


# Below is the products route
@app.route("/api/products")
def products():
    return jsonify({"message": "Welcome to the products route"})

# Below is a route for addition
@app.route ("/api/calc", methods = ["POST"])
def calculator ():
    if request.method == "POST":
        number1= request.form ["number1"]
        number2 = request.form["number2"]
        sum = int(number1) + int ( number2)

        return jsonify({"The answer is " : sum})
    

    @app.route ("/api/simple", methods = ["POST"])
    def calculator ():
        if request.method == "POST":
         principle= request.form ["principle"]
        rate = request.form["rate"]
        time = request.form ["time"]
        simpleinterest = (int(principle)*int(rate)*int(time))/100

        return jsonify({"The Simple Interest is " : simpleinterest})








# Below we run the application
app.run(debug=True)