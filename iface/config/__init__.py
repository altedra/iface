# Config init
from flask import Flask

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'iface'
