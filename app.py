from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Route for displaying the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to receive coordinates
@app.route('/submit-coordinates', methods=['POST'])
def submit_coordinates():
    data = request.get_json()  # Get the JSON data (list of coordinates)
    
    # Get the current date and time to generate a unique file name

    # Define the file path
    file_path = f'coordinates.json'

    # Save the data to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Coordinates saved to {file_path}")

    # Send back a confirmation response
    return jsonify({'status': 'success', 'file_saved': file_path})

if __name__ == '__main__':
    app.run(debug=True)
