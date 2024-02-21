from flask import Flask, render_template

app = Flask(__name__)

#opens hello.html from templates folder
@app.route('/')
def hello():
    return render_template('hello.html')

#this allows us to run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
