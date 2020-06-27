from flask import Flask
app = Flask(__name__)

# Catch all the paths in System 1
@app.route('/', defaults = { 'path': '' })
@app.route('/<path:path>')
def System1(path):
    return f'This is System 1! \
    You requested path: "{path}"'