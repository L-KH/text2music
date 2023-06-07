from flask import Flask, request, jsonify
from flask_cors import CORS
from gradio_client import Client

app = Flask(__name__)
CORS(app)

@app.route('/generate_music', methods=['POST'])
def generate_music():
    try:
        data = request.get_json()
        description = data.get('description')
        numberOfTunes = data.get('numberOfTunes')
        maxLength = data.get('maxLength')
        topP = data.get('topP')
        temperature = data.get('temperature')
        seed = data.get('seed')

        client = Client("https://sander-wood-text-to-music.hf.space/")
        result = client.predict(
            description,
            numberOfTunes,
            maxLength,
            topP,
            temperature,
            seed,
            api_name="/predict"
        )
        return jsonify(result)

    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred during music generation"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
