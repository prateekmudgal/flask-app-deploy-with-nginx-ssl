from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sample Flask App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            nav {
                background-color: #333;
                color: white;
                padding: 1rem 0;
            }
            nav .container {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                padding: 2rem 0;
            }
            h1, h2 {
                margin: 0;
            }
            button {
                padding: 0.5rem 1rem;
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            #message {
                margin-top: 1rem;
                color: green;
            }
        </style>
    </head>
    <body>
        <nav>
            <div class="container">
                <h1>My Flask App</h1>
            </div>
        </nav>
        <div class="container">
            <h2>Welcome to My Flask App</h2>
            <p>This is a sample Flask application with a good interface.</p>
            <button id="clickMe">Click Me</button>
            <p id="message"></p>
        </div>
        <script>
            document.addEventListener('DOMContentLoaded', (event) => {
                const button = document.getElementById('clickMe');
                const message = document.getElementById('message');

                button.addEventListener('click', () => {
                    message.textContent = "Button clicked!";
                });
            });
        </script>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

