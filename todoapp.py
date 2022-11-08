from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import re

app = Flask(__name__)
todo = []


@app.route('/')
def index():
    return render_template('index.html', todo=todo)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['Task']
    priority = request.form['Priority']
    email = request.form['Email']

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    elif not task:
        return redirect('/')
    elif priority == 'Priority':
        return redirect('/')
    else:
        todo.append((task, priority, email))

    print(todo)
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    del todo[:]
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
