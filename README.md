# AI Assistant WebApp

This is an AI assistant web application built using Flask. It leverages various AI capabilities to interact with users, providing support, answering questions, brainstorming ideas, and more.

## Features
- Conversational AI for engaging user interactions
- Support for multiple languages
- Customizable for different use cases
- Easy to deploy and run

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- Flask
- openai

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AmirFaramarzpour/AI-Assistant-WebApp.git
    cd ai-assistant-webapp
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt

    Flask==2.0.1
    flask-cors==3.0.10
    openai==0.27.0
    requests==2.26.0

    ```

3. Run the application:
    ```sh
    Edit the code anf add your own api-key string ""
    python3 app.py
    ```

## Usage
Open your web browser and navigate to `http://localhost:5000` to interact with the AI assistant.

## Contributing
We welcome contributions! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Explanation
This AI assistant web application is designed to facilitate engaging and meaningful interactions with users. Built using Flask, it provides a lightweight and flexible framework for deploying AI-driven conversations.

Key Components:

Flask: The core framework used for building the web application. It handles routing, requests, and rendering HTML templates.

AI Model: The heart of the assistant, responsible for understanding and generating responses based on user input.

OpenAI API: Utilized to leverage advanced AI capabilities for generating text and understanding context.

Flask-CORS: A Flask extension used to handle Cross-Origin Resource Sharing (CORS), ensuring that the web app can be accessed from different origins without issues.

Flow:

The user interacts with the web interface, sending queries or commands.

The Flask server receives the input and processes it.

The AI model generates a response based on the input and context.

The response is sent back to the web interface and displayed to the user.

