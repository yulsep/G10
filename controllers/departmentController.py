from models.departament import Department
from repositories.enrollmentRepository import EnrollmentRepository

class DepartmentController:
    def __init__(self):
        print("Department controller ready")

    def index(self) -> list:
        """
        :return:
        """
        print("Get all")

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        print("Show by id")

    def create (self, department_: dict) -> dict:
        """
        :param department_:
        :return:
        """
        print("Insert")

    def update(self, id_: str, department_: dict) -> dict:
        """

        :param self:
        :param id_:
        :param department_:
        :return:
        """
        print("Update")

    def delete(self, id_: str) -> str:
        """

        :param self:
        :param id_:
        :return:
        """
        print("Delete")

