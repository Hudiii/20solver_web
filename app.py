from flask import Flask, request, jsonify, render_template
from operation import calc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    input_data = data.get('input')
    
    if not input_data or len(input_data) != 4:
        return jsonify({"error": "Input must be a list of four numbers."}), 400
    
    try:
        input_data = list(map(int, input_data))
    except ValueError:
        return jsonify({"error": "All input values must be numbers."}), 400

    operation_result = calc(input_data)
    if operation_result:
        result = []
        count = 0
        for item in operation_result:
            count += 1
            item = item[1:-1]
            result.append(f"{item} = 20")
        return jsonify({"result": result, "total_solutions": count})
    else:
        return jsonify({"result": "Solution not found!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
