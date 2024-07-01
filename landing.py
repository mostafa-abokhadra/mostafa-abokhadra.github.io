from flask import Flask, render_templates
import os
app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(12)

@app.route('/', strict_slashes=False)
def landing ():
    return render_templates('landing.html')

@app.route('/feature', strict_slashes=False)
def feature():
    return render_templates('features.html')

@app.route('/About', strict_slashes=False)
def about():
    return render_templates('about.html')

if __name__ == '__main__':
    app.run(debug=True)