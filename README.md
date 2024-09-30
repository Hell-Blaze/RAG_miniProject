# Research Assistant Web App

## Description
The Research Assistant Web App takes user queries and provides relevant answers based on available resources, such as uploaded research papers. It's designed to offer highly specific, focused answers instead of general, vague results, making it a useful tool for research in particular subject areas.

## Key Features
- **Simple Web Application**: Easy-to-use interface for uploading research papers and querying them.
- **Focused Answers**: Provides relevant and specific answers based on the available documents.
- **Customizable Document Span**: Modify the span of documents to refine answers.

## Setup Instructions
Follow these steps to set up and run the application locally:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Hell-Blaze/RAG_miniProject.git
    cd "path to your directory"/RAG_miniProject
    ```

2. **Install Docker**: 
   Ensure that Docker is installed on your computer. You can download Docker from [here](https://www.docker.com/get-started).

3. **Obtain Gemini API and Pathway Keys**: 
   Get the relevant API keys from the Gemini and Pathway services and place them in a `.env` file.
   ```bash
   GEMINI_API_KEY= 'your_gemini_key'
   PW_KEY= 'your_pathway_api_key'
   ```

5. **Integrate API Keys**: 
   Ensure the keys are integrated into the `app.py` file by referencing the `.env` file.

6. **Create Docker Image**:
   Open a terminal in the repository directory and create the Docker image:
   ```bash
   docker build -t raggem .
   ```

7. **Run Docker Container*:
   Run the Docker container on port 8000:
   For windows:
   ```bash
   docker run -v "${PWD}/data:/app/data" -p 8000:8000 raggem
   ```
   For Linux:
   ```bash
   docker run -v "$(pwd)/data:/app/data" -p 8000:8000 --env-file .env raggem
   ```
   Handling Port Conflicts: If port 8000 is already in use, specify a different port. For example, to use port 8080:
   
8. **Start the Web Server**:
   Open a new terminal navigate to the web_app folder, start the web server by running the following Python script:
   ```bash
   python web.py
   ```

9. **Access the Application**:
    Open your web browser and navigate to the address shown in the terminal (e.g., http://localhost:5001).
    If the ports are not available then assign a free port and make necessary changes in the web.py.

10. **Refer the video instructions**:
    A video tutorial is also available in the repository. The video is based on windows environment so if you are using windows you can refer it. 

## Usage Instructions
This project is in its early stages, serving as a lightweight research assistant application. It helps retrieve answers based on specific research documents uploaded by the user. Please use it accordingly for research and educational purposes.

## Technologies Used
- Docker
- Pathway RAG Pipelines
- Vector Databases and Embeddings
- Python
- HTML (for the web app UI)

## Contribution
This project is educational, and any suggestions or modifications to improve the application are highly welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License
This project does not currently have a license and is intended for educational purposes only.

### Notes:
- Replace `YOUR_USERNAME` and `your-repo-name` in the clone URL with your actual GitHub username and repository name.
- Make sure to explain the `.env` file's content format (e.g., `GEMINI_API_KEY=your_key`).

Feel free to modify this as needed!
   
    
