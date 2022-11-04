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
        return self.enrollment_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        print("Show by id")
        return self.enrollment_repository.find_by_id(id_)

    def create (self, enrollment_: dict) -> dict:
        """
        :param enrollment_:
        :return:
        """
        print("Insert")
        enrollment = Enrollment(enrollment_)
        return self.enrollment_repository.save(enrollment)

    def update(self, id_: str, enrollment_: dict) -> dict:
        """

        :param self:
        :param id_:
        :param enrollment_:
        :return:
        """
        print("Update")
        enrollment = Enrollment(enrollment_)
        return self.enrollment_repository.update(id_, enrollment)

    def delete(self, id_: str) -> str:
        """

        :param self:
        :param id_:
        :return:
        """
        print("Delete" + id_)
        return self.enrollment_repository.delete(id_)

