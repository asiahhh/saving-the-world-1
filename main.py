from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    input = request.form['data']
    if int(input) > 100:
      return render_template('good_job.html')
    else:
      return render_template('a_little_bit_more.html')
  with open('content.txt', 'r') as file: # read only
    intro = file.read()  
  data = None
  if request.method =='POST':
    data = request.form['data']
    data = data # change data
    with open('data.txt', 'a') as file: # add or create file
      file.write(data + '\n')
  return render_template('index.html', data=data, intro=intro)


app.run(host='0.0.0.0', port=81)
