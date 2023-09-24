
from flask import Flask, request, jsonify
from ElasticSearchConfig import ElasticSearchConfig 
from ServiceStatus import ServiceStatus
from HealthCheck import HealthCheck
import json



app = Flask(__name__)
es_config = ElasticSearchConfig()
service_status = ServiceStatus(es_config)
health_check = HealthCheck(es_config)

@app.route('/add', methods=['POST'])
def add_service_status():
    print( request.files)
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']

    # If user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Reading the file content and loading it as JSON
    file_content = file.read()
    try:
        file_json = json.loads(file_content)
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON file'}), 400

    # Passing the JSON content to add_status function
    response = ()

    # Assuming add_status returns a response which can be jsonify
    return jsonify(*service_status.add_status(file_json))


@app.route('/healthcheck', methods=['GET'])
def get_all_status():
    return jsonify(health_check.get_all_status())


@app.route('/healthcheck/<string:service_name>', methods=['GET'])
def get_service_status(service_name):
    return jsonify(health_check.get_service_status(service_name))


if __name__ == '__main__':
    app.run(debug=True, port=5001)