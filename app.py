from flask import Flask, render_template, request, jsonify
from pythonObjects.main import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')


@app.route('/solution', methods=['POST','GET'])
def solution():
    data = request.get_json()
    solution = get_solution(data)
    str_sol = "{ "
    for i in solution:
        if i.isalpha():
            str_sol += str(i) + " "
    str_sol += "}"
    return str_sol

if __name__ == '__main__':
	app.run(debug=True)