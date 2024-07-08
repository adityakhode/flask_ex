import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_folder='public', template_folder='views')
app.secret_key = os.environ.get('SECRET')

uploaded_file_path = None  # Store the uploaded file path globally

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_file_path

    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    # Save the uploaded file to a temporary location
    file.save(os.path.join(os.getcwd(), file.filename))
    uploaded_file_path = os.path.join(os.getcwd(), file.filename)

    return 'File successfully uploaded.'

@app.route('/convert', methods=['POST'])
def convert_file():
    global uploaded_file_path

    if uploaded_file_path:
        # Perform your conversion logic here
        # For demonstration, let's just read and echo back the content
        with open(uploaded_file_path, 'r') as f:
            content = f.read()
        return content
    else:
        return 'No file uploaded or file path is missing.'

@app.route('/print', methods=['POST'])
def print_hello():
    print("hello")
    return 'Printed hello.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
