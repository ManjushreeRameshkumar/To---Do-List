from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect('/')

@app.route('/done/<int:index>')
def done(index):
    tasks.pop(index)     # remove the task when completed
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
