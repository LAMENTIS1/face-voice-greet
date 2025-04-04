from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import edge_tts
import asyncio
import uuid
import os 
import requests  # For calling the Flowise API

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Flowise API URL
FLOWISE_API_URL = "https://srivatsavdamaraju-flowise.hf.space/api/v1/prediction/2875301a-c26f-4bd5-ab10-71fa13393541"

# Ensure the "static" folder exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def home():
    # Serve the HTML template
    return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process():
#     # Get the transcript from the request
#     data = request.json
#     transcript = data.get('transcript', '')

#     # Send the transcript to the Flowise API
#     try:
#         flowise_response = query_flowise({"question": transcript})
#         response_text = flowise_response.get("text", "No response from Flowise API")
#     except Exception as e:
#         print(f"Error querying Flowise API: {e}")
#         response_text = "Sorry, there was an error processing your request."

#     # Generate a unique filename for the audio
#     unique_id = str(uuid.uuid4())
#     audio_file_path = f"static/response_{unique_id}.mp3"

#     # Generate audio using Edge TTS
#     asyncio.run(generate_audio(response_text, audio_file_path))

#     # Return the response text and the URL to the audio file
#     return jsonify({
#         'text': response_text,
#         'audio_url': f'/static/response_{unique_id}.mp3'
#     })

# async def generate_audio(text, output_file):
#     try:
#         # Use Edge TTS to generate audio
#         communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
#         await communicate.save(output_file)
#         print(f"Audio saved to {output_file}")
#     except Exception as e:
#         print(f"Error generating audio: {e}")

# def query_flowise(payload):
#     # Query the Flowise API
#     response = requests.post(FLOWISE_API_URL, json=payload)
#     if response.status_code != 200:
#         raise Exception(f"Flowise API returned status code: {response.status_code}")
#     return response.json()

# @app.route('/static/<filename>')
# def serve_static(filename):
#     # Serve static files (e.g., audio files)
#     return app.send_static_file(filename)





# @app.route('/js_detected_faces', methods=['POST'])
# def handle_detected_faces():
#     try:
#         # Get the array of detected faces directly from the request body
#         detected_faces = request.get_json()
#         if isinstance(detected_faces, list):  # Ensure the data is a list
#             print("Detected Faces:", detected_faces)
#             return jsonify({"status": "success", "message": "Faces received", "faces": detected_faces})
#         else:
#             return jsonify({"status": "error", "message": "Invalid data format. Expected an array of faces."}), 400
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

