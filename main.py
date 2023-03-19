from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    with open('content.txt', 'r') as file:
        intro = file.read()
    data = None
    if request.method == 'POST':
        data = request.form['data']
        data = int(data) # convert data to integer
        if data < 100:
            return render_template('less.html')
        elif 100 <= data < 1440:
            return render_template('middle.html')
        else:
            return render_template('more.html')
    return render_template('index.html', data=data, intro=intro)

app.run(host='0.0.0.0', port=81)
