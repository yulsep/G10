from flask import Blueprint, jsonify
from flask import request

from controllers.enrollmentController import EnrollmentController

enrollment_blueprints = Blueprint('enrollment_blueprints', __name__)
enrollment_controller = EnrollmentController()


@enrollment_blueprints.route("/enrollment/all", methods=['GET'])
def get_all_enrollments():
    response = enrollment_controller.index()
    return jsonify(response), 200


@enrollment_blueprints.route("/enrollment/<string:id_>", methods=['GET'])
def get_enrollment_by_id(id_):
    response = enrollment_controller.show(id_)
    return jsonify(response), 200


@enrollment_blueprints.route("/enrollment/insert", methods=['POST'])
def insert_enrollment():
    enrollment = request.get_json()
    response = enrollment_controller.create(enrollment)
    return jsonify(response), 201


@enrollment_blueprints.route("/enrollment/update/<string:id_>", methods=['PATCH'])
def update_enrollment(id_):
    enrollment = request.get_json()
    response = enrollment_controller.update(id_, enrollment)
    return jsonify(response), 201


@enrollment_blueprints.route("/enrollment/delete/<string:id_>", methods=['DELETE'])
def delete_enrollment(id_):
    response = enrollment_controller.delete(id_)
    return jsonify(response), 204
