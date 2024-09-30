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
    git clone https://github.com/YOUR_USERNAME/your-repo-name.git
    cd your-repo-name
    ```

2. **Install Docker**: 
   Ensure that Docker is installed on your computer. You can download Docker from [here](https://www.docker.com/get-started).

3. **Obtain Gemini API and Pathway Keys**: 
   Get the relevant API keys from the Gemini and Pathway services and place them in a `.env` file.

4. **Integrate API Keys**: 
   Ensure the keys are integrated into the `app.py` file by referencing the `.env` file.

5. **Create Docker Image**:
   Open a terminal in the repository directory and create the Docker image:
   ```bash
   docker build -t research-assistant-app .
