from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')#testing domain 
def hello():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()