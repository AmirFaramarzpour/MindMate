from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO, emit
import openai

app = Flask(__name__)
socketio = SocketIO(app)
openai.api_key = "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"  # Make sure to replace this with your actual OpenAI API key

@app.route('/api/ai', methods=['POST'])
def api_ai_response():
    prompt = request.json.get('prompt', '')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=8192
        )
        result = response['choices'][0]['message']['content'].strip()
        if not result:
            result = "Sorry, I couldn't generate a response. Please try again with a different prompt."
        return jsonify({'response': result})
    except openai.error.OpenAIError as e:
        return jsonify({'error': str(e)})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
