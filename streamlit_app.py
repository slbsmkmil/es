from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    html_content = '''
    
