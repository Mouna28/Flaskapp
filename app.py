from flask import Flask
app= Flask(__name__)
@app.route('/')
def hello():
    return '<h1>Hello! fromm docker</h1><p>this is a flask apprunning inside a container</p>'

@app.route('/health')
def health():
    return '<h1>Hello health is good</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)