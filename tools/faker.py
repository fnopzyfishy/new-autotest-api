from faker import Faker

class Fake:
    """
    Класс для генерации случайных тестовых данных
    """
    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker который будет использоваться для генерации данных
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст
        :return:
        """
        return self.faker.text()

    def uuid4(self):
        """
        Генерирует данные в формате uuid4
        :return:
        """
        return self.faker.uuid4()

    def email(self) -> str:
        """
        Генерирует случайный email
        :return:
        """
        return self.faker.email()

    def sentence(self) -> str:
        """
        Генерирует случайное предложение
        :return:
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль
        :return:
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию
        :return:
        """
        return self.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя
        :return:
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество
        :return:
        """
        return self.faker.middle_name()

    def estimated_time(self) -> str:
        """
        Генерирует строку с предпологаемым временем
        :return:
        """
        return f"{self.integer(1, 10)} weeks"

    def integer(self, start: int=1, end: int=100) -> int:
        """
        Генерирует случайное число в заданном диапазоне

        :param start:
        :param end:
        :return:
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Генерирует случайный максимальный балл в диапазоне от 50 до 100

        :return:
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Генерирует случайный минимальный балл в диапазоне от 1 до 30

        :return:
        """
        return self.integer(1, 30)


fake = Fake(faker=Faker())