from flask import Flask
app = Flask(__name__)

# All paths except for /control are caught by 
# the System2 function. Let's pretend that 
# this is the control panel, which we do not 
# want to expose
@app.route('/control', defaults = { 'path': '' })
@app.route('/control/<path:path>')
def control(path):
    return 'Director cats do not want the \
        public to see this. Internal \
            eyes only!'

@app.route('/', defaults = { 'path': '' })
@app.route('/<path:path>')
def System2(path):
    return f'This is System 2! \
        You requested path: "{path}"'