from models.student import Student
from repositories.studentRepository import StudentRepository


class StudentController:
    def __init__(self):
        print("Student controller ready")
        self.student_repository = StudentRepository()

    def index(self) -> list:
        """
        This method gets all the students into the DB
        :return: student's list
        """
        return self.student_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        print("Show by id")
        return self.student_repository.find_by_id(id_)

    def create (self, student_: dict) -> dict:
        """
        :param student_:
        :return:
        """
        print("Insert")
        student = Student(student_)
        return self.student_repository.save(student)

    def update(self, id_: str, student_: dict) -> dict:
        """

        :param id_:
        :param student_:
        :return:
        """
        print("Update")
        student = Student(student_)
        return self.student_repository.update(id_, student)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete" + id_)
        return self.student_repository.delete(id_)
