from flask import Flask, render_template
import os
app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(12)

@app.route('/', strict_slashes=False)
def index ():
    return render_template('index.html')

@app.route('/feature', strict_slashes=False)
def feature():
    return render_template('features.html')

@app.route('/About', strict_slashes=False)
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)