from flask import Flask
import os
app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(12)
if __name__ == '__main__':
    app.run(debug=True)