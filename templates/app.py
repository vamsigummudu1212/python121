from flask import Flask, render_template, request, jsonify
import subprocess
import threading

app = Flask(__name__)

# Global variable to hold the subprocess
process = None

def run_python_program():
    global process
    process = subprocess.Popen(['python', 'python.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/run_program', methods=['POST'])
def run_program():
    # Execute your Python program here
    global process
    if process is None or process.poll() is not None:  # If no process is running or the previous one has finished
        thread = threading.Thread(target=run_python_program)
        thread.start()
        return jsonify({'message': 'Python program started.'})
    else:
        return jsonify({'message': 'Python program is already running.'})

@app.route('/stop_program', methods=['POST'])
def stop_program():
    global process
    if process and process.poll() is None:  # If a process is running
        process.terminate()  # Terminate the process
        process = None  # Reset the global variable
        return jsonify({'message': 'Python program stopped.'})
    else:
        return jsonify({'message': 'No running Python program to stop.'})

if __name__ == '__main__':
    app.run(debug=True)
