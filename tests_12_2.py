# импорт библиотек и файлов
import unittest
import runner_and_tournament as rt


class TournamentTest(unittest.TestCase):  # класс TournamentTest, наследованный от TestCase
    all_results = None

    # Метод создания атрибута класса all_results
    # словарь в который будут сохраняться результаты всех тестов.
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    # метод создания 3 объектов для тестов
    def setUp(self):
        self.run1 = rt.Runner('Усэйн', 10)
        self.run2 = rt.Runner('Андрей', 9)
        self.run3 = rt.Runner('Ник', 3)

    # метод, где выводятся all_results (результаты теста) по очереди в столбец
    @classmethod
    def tearDownClass(cls):
        result = {}  # объявление словаря
        for testkey, testval in cls.all_results.items():  # цикл перебора тестов
            print(f'TEST: {testkey}')  # вывод на консоль типа теста
            for key, val in testval.items():  # цикл создания словаря участников теста
                result[key] = str(val.name)  # ввод данных результатов теста
            print(result)  # вывод на консоль участников теста по порядку

    def testrun_1(self):  # метод 1-го теста между участником 1 и 3
        # обращение к функции Tournament в файле runner_and_tournament
        run_1 = rt.Tournament(90, self.run1, self.run3)
        # получение результатов теста run1
        finish = run_1.start()
        # метод из класса TestCase в модуле unittest, который проверяет, истинность выражения
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        # присвоение self.all_results результатов теста между участниками
        self.all_results[f'Результат {self.run1} и {self.run3}'] = finish

    def testrun_2(self):  # метод 2-го теста между участником 2 и 3
        run_1 = rt.Tournament(90, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run2} и {self.run3}'] = finish

    def testrun_3(self):  # метод 3-го теста между 3-мя участниками
        run_1 = rt.Tournament(90, self.run1, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1}, {self.run2} и {self.run3}'] = finish


if __name__ == "__main__":
    unittest.main()
