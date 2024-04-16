from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/run_program', methods=['POST'])
def run_program():
    # Execute your Python program here
    result = subprocess.run(['python', 'python.py'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
