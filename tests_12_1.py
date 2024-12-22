# импорт библиотек и файлов
import unittest
import runner as rr


class RunnerTest(unittest.TestCase):  # класс Runner, наследуемый от TestCase из модуля unittest
    def test_walk(self):              # метод test_walk
        walk_ = rr.Runner('man')      # объект класса Runner с произвольным именем
        for _ in range(10):           # вызов метода walk у этого объекта 10 раз
            walk_.walk()
        self.assertEqual(walk_.distance, 50)  # метод assertEqual сравнивает distance объекта со значением 50
        print('Test "walk" OK')       # вывод на консоль если все правильно

    def test_run(self):               # метод test_run
        run_ = rr.Runner('man')       # объект класса Runner с произвольным именем
        for _ in range(10):           # вызов метода run у этого объекта 10 раз
            run_.run()
        self.assertEqual(run_.distance, 100)  # метод assertEqual сравнивает distance объекта со значением 100
        print('Test "run" OK')        # вывод на консоль если все правильно

    def test_challenge(self):         # метод test_challenge
        # создаются 2 объекта класса Runner с произвольными именами
        challenge1 = rr.Runner('man_first')
        challenge2 = rr.Runner('man_second')
        # 10 раз у объектов вызываются методы run и walk соответственно
        for _ in range(10):
            challenge1.run()
            challenge2.walk()
        # метод assertNotEqual, чтобы убедится в неравенстве результатов
        self.assertNotEqual(challenge1.distance, challenge2.distance)
        print('Test "challenge" OK')  # вывод на консоль если все правильно


if __name__ == '__main__':
    unittest.main()
