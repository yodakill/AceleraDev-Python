from abc import ABC, abstractmethod


class Department:
    """
    self.name = name -> Nome Departamento
    self.code = code -> Código do Departamento
    """
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    """
    self.__department = department -> Departamento
    self.code = code -> Código do empregado
    self.name = name -> Nome do empregado
    self.salary = salary -> Salário do empregado
    self.workDay = 8 -> Horas De Trabalho
    """

    def __init__(self, code, name, salary, department):
        self.__department = department
        self.code = code
        self.name = name
        self.salary = salary
        self.workDay = 8

    @abstractmethod
    def calc_bonus(self):
        """Retorna bonus"""
        pass

    def get_hours(self):
        """Retorna quantidade de horas trabalhadas"""
        return self.workDay

    def get_department(self):
        """Retorna Departamento"""
        return self.__department.name

    def set_department(self, department, department_code):
        """Modifica o departamento e intância um novo"""
        self.__departament = Department(department, department_code)


class Manager(Employee):
    def __init__(self, code, name, salary):
        """Herda a classe Employee - duvidas https://realpython.com/python-super/"""
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        """Herda a classe Employee - duvidas https://realpython.com/python-super/"""
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def get_sales(self):
        """Retorna total das vendas"""
        return self.__sales

    def calc_bonus(self):
        """Incrementa 15% sobre as vendas """
        return self.__sales * 0.15

    def put_sales(self, sale):
        """
        sale -> Valor Venda
        self.__sales += sale -> Incrementa total de vendas
        """
        self.__sales += sale
