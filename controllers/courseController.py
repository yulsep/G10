from models.course import Course


class CourseController:
    def __init__(self):
        print("Course controller ready")

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

    def create (self, course_: dict) -> dict:
        """
        :param course_:
        :return:
        """
        print("Insert")

    def update(self, id_: str, course_: dict) -> dict:
        """

        :param self:
        :param id_:
        :param course_:
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