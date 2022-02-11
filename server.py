from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #just to test
def hello_world():
    return render_template('index.html', number=8, number2=8)

@app.route('/4') #just to test
def hello_world2():
    return render_template('index.html', number=4, number2=8)

@app.route('/<int:number>/<int:number2>') #just to test
def hello_world3(number, number2):
    return render_template('index.html', number=number, number2=number2)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
