import unittest
from tests_12_3 import RunnerTest, TournamentTest

class TestSuite(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        self.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
        self.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

if __name__ == "__main__":
    suite = TestSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)