from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
