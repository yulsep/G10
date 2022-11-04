from models.departament import Department
from repositories.departmentRepository import DepartmentRepository


class DepartmentController:
    def __init__(self):
        print("Department controller ready")
        self.department_repository = DepartmentRepository()

    def index(self) -> list:
        """
        :return:
        """
        print("Get all")
        return self.department_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        print("Show by id")
        return self.department_repository.find_by_id(id_)

    def create (self, department_: dict) -> dict:
        """
        :param department_:
        :return:
        """
        print("Insert")
        department = Department(department_)
        return self.department_repository.save(department)

    def update(self, id_: str, department_: dict) -> dict:
        """

        :param self:
        :param id_:
        :param department_:
        :return:
        """
        print("Update")
        department = Department(department_)
        return self.department_repository.update(id_, department)

    def delete(self, id_: str) -> str:
        """

        :param self:
        :param id_:
        :return:
        """
        print("Delete")
        return self.department_repository.delete(id_)

