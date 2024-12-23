# импорт необходимых библиотек и файлов
import unittest
import logging
import rt_with_exceptions as rr

""" Желательно basicConfig указывать после импортов до написания кода программы
    basicConfig настроен на параметры:
       1. Уровень - INFO
       2. Режим - запись с заменой('w')
       3. Название файла - runner_tests.log
       4. Кодировка - UTF-8
       5. Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования."""
logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest1(unittest.TestCase):

    def test_walk(self):    # метод test_walk
        try:                # блок try проверяет код на наличие исключений
            # объект класса Runner с произвольным именем
            walk_ = rr.Runner('man', -5)
            # вызов метода walk у этого объекта 10 раз
            for _ in range(10):
                walk_.walk()
            # методом assertEqual сравниваем distance этого объекта со значением 50
            self.assertEqual(walk_.distance, 50)
            # логирование INFO
            logging.info('"test_walk" выполнен успешно')
        # блок except выполняется, если в блоке try нашлась ошибка значения переменной
        except ValueError as e:
            # логирование на уровне WARNING
            logging.warning(f'Неверная скорость для Runner. \n{e}')

    def test_run(self):     # метод test_run
        try:                # блок try проверяет код на наличие исключений
            # объект класса Runner с произвольным именем
            run_ = rr.Runner(5)
            # вызов метода run у этого объекта 10 раз
            for _ in range(10):
                run_.run()
            # методом assertEqual сравниваем distance этого объекта со значением 100
            self.assertEqual(run_.distance, 100)
            # логирование INFO
            logging.info('"test_run" выполнен успешно')
        # блок except выполняется, если в блоке try нашлась ошибка типа переменной
        except TypeError as e:
            # логирование на уровне WARNING
            logging.warning(f'Неверный тип данных для объекта Runner. \n{e}')


if __name__ == '__main__':
    unittest.main()
