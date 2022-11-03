from flask import Blueprint, jsonify
from flask import request

from controllers.studentController import StudentController

student_blueprints = Blueprint('student_blueprints', __name__)
student_controller = StudentController()


@student_blueprints.route("/student/all", methods=['GET'])
def get_all_students():
    response = student_controller.index()
    return jsonify(response), 200


@student_blueprints.route("/student/<string:id_>", methods=['GET'])
def get_student_by_id(id_):
    response = student_controller.show(id_)
    return jsonify(response), 200


@student_blueprints.route("/student/insert", methods=['POST'])
def insert_student():
    student = request.get_json()
    response = student_controller.create(student)
    return jsonify(response), 201


@student_blueprints.route("/student/update/<string:id_>", methods=['PATCH'])
def update_student(id_):
    student = request.get_json()
    response = student_controller.update(id_, student)
    return jsonify(response), 201


@student_blueprints.route("/student/delete/<string:id_>", methods=['DELETE'])
def delete_student(id_):
    response = student_controller.delete(id_)
    return jsonify(response), 204
