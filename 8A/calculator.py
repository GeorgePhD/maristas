from flask import Flask, render_template, request

app = Flask(__name__)

# Define mathematical functions
def add(a, b):
    result = a + b
    return int(result) if result.is_integer() else result

def subtract(a, b):
    result = a - b
    return int(result) if result.is_integer() else result

def multiply(a, b):
    result = a * b
    return int(result) if result.is_integer() else result

def divide(a, b):
    if b == 0:
        return "come on mate! you know you can't do that."
    result = a / b
    return int(result) if result.is_integer() else result

# Define the route for the homepage
@app.route('/')

def index():
    return render_template('index.html')

# Define the route for calculation
@app.route('/calculate', methods=['POST'])

def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        result = "Invalid operation"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
