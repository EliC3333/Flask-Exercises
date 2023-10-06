from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now().strftime('%A, %B %d, %Y %H:%M:%S')
    return render_template_string("""
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            <title>Current Time</title>
            <style>
                html, body {
                    height: 100%;
                    margin: 0;
                    font-family: Arial, sans-serif;
                }
                .container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100%;
                }
                .container p {
                    font-size: 88px; 
                }
            </style>
          </head>
          <body>
            <div class="container">
              <p>The current date time is: {{ current_time }}</p>
            </div>
          </body>
        </html>
    """, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)