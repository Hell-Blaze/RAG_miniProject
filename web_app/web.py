from flask import Flask, render_template, request, jsonify
import requests
import subprocess
import os

app = Flask(__name__)

# Store uploaded documents
uploaded_documents=[]
# Ensure the uploads directory exists

os.chdir("..")
if not os.path.exists('data'):
    os.makedirs('data')

UPLOAD_FOLDER = os.path.join(os.getcwd(), "data")
uploaded_documents += os.listdir(UPLOAD_FOLDER)

os.chdir("web_app")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question')
    
    # Prepare the PowerShell command
    ps_command = f"Invoke-RestMethod -Uri 'http://localhost:8000/v1/pw_ai_answer' -Method POST -ContentType 'application/json' -Body '{{\"prompt\": \"{question}\"}}'"

    try:
        # Execute the PowerShell command and capture the output
        result = subprocess.run(['powershell', '-Command', ps_command], capture_output=True, text=True, check=True)
        response_output = result.stdout  # Capture the response from the RAG service
    except subprocess.CalledProcessError as e:
        response_output = f"Error: {e.stderr} \nPlease refresh the Webpage."      


    return jsonify({'answer': response_output})

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['document']
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)  # Save the file to the uploads directory
        if(file.filename not in uploaded_documents):
            uploaded_documents.append(file.filename)
        return jsonify({'message': 'File uploaded successfully!'})
    return jsonify({'message': 'No file uploaded.'}), 400

@app.route('/documents', methods=['GET'])
def list_documents():
    return jsonify(uploaded_documents)

@app.route('/delete_document', methods=['POST'])
def delete_document():
    filename = request.json.get('filename')
    if filename in uploaded_documents:
        uploaded_documents.remove(filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"message": "File deleted successfully."})
    return jsonify({"message": "File not found."}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run Flask app on port 5001
