
from flask import Flask, request, jsonify, send_file
import os
from utils import clean_csv

app = Flask(__name__)
UPLOAD_FOLDER = 'cleaned_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return 'Automated Data Cleaning API is running!'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    try:
        df_cleaned = clean_csv(file)
        output_path = os.path.join(UPLOAD_FOLDER, 'cleaned.csv')
        df_cleaned.to_csv(output_path, index=False)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
