from models.course import Course
from repositories.courseRepository import CourseRepository


class CourseController:
    def __init__(self):
        print("Course controller ready")
        self.course_repository = CourseRepository()

    def index(self) -> list:
        """
        :return:
        """
        print("Get all")
        return self.course_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        print("Show by id")
        return self.course_repository.find_by_id(id_)

    def create (self, course_: dict) -> dict:
        """
        :param course_:
        :return:
        """
        print("Insert")
        course = Course(course_)
        return self.course_repository.save(course)

    def update(self, id_: str, course_: dict) -> dict:
        """

        :param self:
        :param id_:
        :param course_:
        :return:
        """
        print("Update")
        course = Course(course_)
        return self.course_repository.update(id_, course)

    def delete(self, id_: str) -> str:
        """

        :param self:
        :param id_:
        :return:
        """
        print("Delete")
        return self.course_repository.delete(id_)
