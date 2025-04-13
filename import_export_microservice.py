from flask import Flask, request, jsonify
import json

app = Flask(__name__)

file_name = 'degreeplan.json'

@app.route('/save_degree_plan', methods=['POST'])
def save_degree_plan():
    data = request.get_json()

    quarters = data['quarters']
    degreePlan = data['degreePlan']

    with open(file_name, 'w') as file:
        file.write(json.dumps({"quarters":quarters, "degreePlan": degreePlan}))
    
    return jsonify({"message":"Degree Plan saved!"})

@app.route(('/load_degree_plan'), methods=['GET'])
def load_degree_plan():

    with open(file_name, 'r') as file:
        data = json.load(file)
    
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5004)