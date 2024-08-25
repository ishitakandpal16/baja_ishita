from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample operation code (this could be generated dynamically in a real scenario)
OPERATION_CODE = "ABC123"

def get_highest_lowercase(alphabets):
    # Filter out lowercase letters and find the highest one
    lowercase_letters = [ch for ch in alphabets if ch.islower()]
    if lowercase_letters:
        return max(lowercase_letters)
    return None

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        data = request.get_json()
        
        # Extract data from JSON
        user_id = data.get('user_id')
        college_email = data.get('college_email')
        roll_number = data.get('roll_number')
        numbers_array = data.get('numbers', [])
        alphabets_array = data.get('alphabets', [])
        
        # Find the highest lowercase alphabet
        highest_lowercase = get_highest_lowercase(alphabets_array)
        
        # Prepare the response
        response = {
            'status': 'success',
            'user_id': user_id,
            'college_email': college_email,
            'roll_number': roll_number,
            'numbers_array': numbers_array,
            'alphabets_array': alphabets_array,
            'highest_lowercase': highest_lowercase
        }
        return jsonify(response), 200

    elif request.method == 'GET':
        return jsonify({'operation_code': OPERATION_CODE}), 200

@app.route('/operation_code', methods=['GET'])
def operation_code():
    return jsonify({'operation_code': OPERATION_CODE}), 200

if __name__ == '__main__':
    app.run(debug=True)