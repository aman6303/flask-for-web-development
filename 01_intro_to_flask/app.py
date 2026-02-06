from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1> Welcome to home</h1>"

@app.route("/about")
def about():
    return "<h1> Welcome to about section"

# example of path parameter

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1> Welcome {name.title()} to our site </h1>"

# example of integer path parameter
@app.route("/addition/<int:num>")
def addition(num):
	return f"<h1>Input is {num}, Output is {num + 10}</h1>"

# example of two integer path param
@app.route("/addition2/<int:num1>/<int:num2>")
def addition2(num1, num2):
    return f"<h1> the sum of these numbers are {num1+num2} </h1>"


if __name__ == "__main__":
    app.run(debug=True)
