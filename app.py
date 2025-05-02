from flask import Flask, request, jsonify
from core import MyBigNumber  # Import your class

app = Flask(__name__)
calculator = MyBigNumber()

@app.route('/sum', methods=['POST'])
def calculate_sum():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input
        if not data or 'num1' not in data or 'num2' not in data:
            return jsonify({"error": "Missing parameters. Required: num1, num2"}), 400
        
        num1 = str(data['num1'])
        num2 = str(data['num2'])
        
        # Calculate sum using your class
        result = calculator.sum(num1, num2)
        
        return jsonify({
            "result": result,
            "num1": num1,
            "num2": num2
        }), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)