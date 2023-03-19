from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  with open('content.txt', 'r') as file: # read only
    intro = file.read()  
  data = None
  if request.method =='POST':
    data = request.form['data']
    data = data # change data
    with open('data.txt', 'a') as file: # add or create file
      file.write(data + '\n')
  return render_template('index.html', data=data, intro=intro)
  if request.method == 'POST':
    data = request.form['data']
    if data < 100:
      return render_template('less.html')
    elif 100 <= data < 1440:
      return render_template('more.html')
    else:
      return render_template('middle.html')


app.run(host='0.0.0.0', port=81)
