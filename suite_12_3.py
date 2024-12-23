# TestSuit
# импорт необходимых библиотек и файлов
import unittest
import tests_12_3

# объявление переменной test_suite объекта TestSuite модуля unittest
test_suite = unittest.TestSuite()
# Добавление тестов RunnerTest и TournamentTest в TestSuit.
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

# Создание объекта класса TextTestRunner, с аргументом verbosity=2.
runner = unittest.TextTestRunner(verbosity=2)
# запуск объекта runner
runner.run(test_suite)
