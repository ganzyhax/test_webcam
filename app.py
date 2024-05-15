from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/take_photo', methods=['POST'])
def take_photo():
    # Retrieve image data from the request
    image_data = request.json.get('image_data')

    # Decode base64-encoded image data
    image_data_decoded = base64.b64decode(image_data.split(',')[1])

    # Write the decoded image data to a file
    with open('captured_photo.png', 'wb') as f:
        f.write(image_data_decoded)

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4444)
