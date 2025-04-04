from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/js_detected_faces', methods=['POST'])
def handle_detected_faces():
    try:
        # Get the array of detected faces directly from the request body
        detected_faces = request.get_json()
        if isinstance(detected_faces, list):  # Ensure the data is a list
            print("Detected Faces:", detected_faces)
            return jsonify({"status": "success", "message": "Faces received", "faces": detected_faces})
        else:
            return jsonify({"status": "error", "message": "Invalid data format. Expected an array of faces."}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)