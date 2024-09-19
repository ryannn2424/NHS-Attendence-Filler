import csv
from flask import Flask, request
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

class CSVParser:
    def __init__(self, file):
        self.file = file

    def parse(self):
        # Decode the file content to a string
        file_content = self.file.read().decode('utf-8')
        reader = csv.reader(file_content.splitlines())
        for row in reader:
            print(row)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    parser = CSVParser(file)
    parser.parse()
    return 'File successfully uploaded and parsed', 200

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Starting mainloop...')
    app.run(debug=True)