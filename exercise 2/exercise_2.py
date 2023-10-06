# Import necessary modules from the Flask library
from flask import Flask, render_template, request, url_for

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL and specify it should respond to GET requests
@app.route('/', methods=['GET'])
def index():
    # Render the 'index.html' template
    return render_template('index.html')

# Define a route for the '/check' URL and specify it should respond to GET requests
@app.route('/check', methods=['GET'])
def check_number():
    # Retrieve the 'number' parameter from the query string of the request
    number = request.args.get('number')

    # Check if 'number' parameter is provided
    if not number:
        message = "No number provided!"
        kind = None
    else:
        # Attempt to parse 'number' to an integer
        try:
            num = int(number)
            
            # Check if the parsed number is even or odd
            if num % 2 == 0:
                message = f"{num} is an even number."
                kind = 'even'
            else:
                message = f"{num} is an odd number."
                kind = 'odd'
        except ValueError:
            # Handle the case where 'number' is not a valid integer
            message = "That's not an integer!"
            kind = None

    # Render the 'result.html' template, passing the message and kind variables to it
    return render_template('result.html', message=message, kind=kind)

# If this script is run as the main module, start the Flask application with debugging enabled
if __name__ == '__main__':
    app.run(debug=True)