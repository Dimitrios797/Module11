# tests_12_4.py
import logging
import unittest
import traceback  # Импортируем модуль для получения трассировки
from runner import Runner  # Импортируем класс Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            # Попытка создать объект Runner с отрицательной скоростью
            runner = Runner("Вася", -5)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            logging.error(traceback.format_exc())  # Записываем трассировку ошибки
            self.assertEqual(str(e), "Скорость не может быть отрицательной, сейчас -5")
        else:
            logging.info('"test_walk" выполнен успешно')
            self.fail("Expected ValueError not raised")

    def test_run(self):
        try:
            # Попытка создать объект Runner с неверным типом для имени
            runner = Runner(123, 10)  # Передаем число вместо строки
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.error(traceback.format_exc())  # Записываем трассировку ошибки
            self.assertEqual(str(e), "Имя может быть только строкой, передано int")
        else:
            logging.info('"test_run" выполнен успешно')
            self.fail("Expected TypeError not raised")


if __name__ == "__main__":
    unittest.main()