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
    tasks.pop(index)     
    return redirect('/')

@app.route('/edit/<int:index>')
def edit(index):
    task = tasks[index]
    return render_template("edit.html", task=task, index=index)

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    new_task = request.form['task']
    tasks[index] = new_task
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
