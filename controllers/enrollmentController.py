from models.enrollment import Enrollment
from repositories.enrollmentRepository import EnrollmentRepository


class EnrollmentController:
    def __init__(self):
        print("Enrollment controller ready")
        self.enrollment_repository = EnrollmentRepository()

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

    def create (self, enrollment: dict) -> dict:
        """
        :param enrollment:
        :return:
        """
        print("Insert")

    def update(self, id_: str, enrollment_: dict) -> dict:
        """

        :param self:
        :param id_:
        :param enrollment_:
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
