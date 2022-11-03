import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.enrollmentBlueprints import  enrollment_blueprints
from blueprints.courseBlueprints import course_blueprints
from blueprints.studentBlueprints import student_blueprints
from blueprints.departmentBlueprints import department_blueprints


app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(course_blueprints)
app.register_blueprint(department_blueprints)
app.register_blueprint(enrollment_blueprints)
app.register_blueprint(student_blueprints)


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Welcome to academic services for G10"}
    return jsonify(response)


# ===================== Config and execution code =============================#
def load_file_config():
    with open("config.json", "r") as config:
        data = json.load(config)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
