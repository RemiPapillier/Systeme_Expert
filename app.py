from flask import Flask, render_template, request
from pythonObjects.main import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')


@app.route('/create_eq', methods=['POST','GET'])
def create_eq():
    data = request.values
    premisse, conclusion = data['premisse'], data['conclusion']
    add_eq(premisse, conclusion)
    return data

@app.route('/create_hyp', methods=['POST','GET'])
def create_hyp():
    data = request.values
    hypothese = data['hypothese']
    add_hyp(hypothese)
    return data

@app.route('/generate_solutions', methods=['POST','GET'])
def generate_solutions():
    solution = get_solution()
    str_sol = "{ "
    for i in solution:
        if i.isalpha():
            str_sol += str(i) + " "
    str_sol += "}"
    return str_sol

@app.route('/reset', methods=['POST','GET'])
def reset():
    reset_systeme()
    return "ok"

if __name__ == '__main__':
	app.run(debug=True)