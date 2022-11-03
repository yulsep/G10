from models.student import Student


class StudentController:
    def __init__(self):
        print("Student controller ready")

    def index(self) -> list:
        """
        :return:
        """
        print("Get all")
        data = {
            "_id": "abc123",
            "names": "Pepita",
            "lastname": "Perez",
            "persona_id": "123456",
        }
        return [data]

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        print("Show by id")
        data = {
            "_id": id_,
            "names": "Pepita",
            "lastname": "Perez",
            "persona_id": "123456",
        }
        return [data]

    def create (self, student_: dict) -> dict:
        """
        :param student_:
        :return:
        """
        print("Insert")
        student = Student(student_)
        return student.__dict__

    def update(self, id_: str, student_: dict) -> dict:
        """

        :param id_:
        :param student_:
        :return:
        """
        print("Update")
        data = student_
        data['_id'] = id_
        student = Student(student_)
        return student.__dict__

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete" + id_)
        return {"Delete count": 1}
