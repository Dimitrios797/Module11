import unittest


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def walk(self):
        self.distance += self.speed * 0.5  # Assuming walking is half the speed

    def run(self):
        self.distance += self.speed  # Running is at full speed

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)  # Use the name as the hash value

    def __repr__(self):
        return f"Runner(name='{self.name}', speed={self.speed})"


class Tournament:
    def __init__(self, distance):
        self.distance = distance
        self.runners = []

    def add_runner(self, runner):
        self.runners.append(runner)

    def start(self):
        results = {}
        for runner in self.runners:
            time_taken = self.distance / runner.speed
            results[runner] = time_taken
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1]))
        return {i + 1: runner.name for i, runner in enumerate(sorted_results.keys())}


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_tournament_usain_nick(self):
        tournament = Tournament(90)
        tournament.add_runner(self.runner1)
        tournament.add_runner(self.runner3)

        results = tournament.start()
        TournamentTest.all_results[1] = results

        # Nick should always be last due to lower speed
        self.assertTrue(results[max(results.keys())] == "Nick")

    def test_tournament_andrey_nick(self):
        tournament = Tournament(90)
        tournament.add_runner(self.runner2)
        tournament.add_runner(self.runner3)

        results = tournament.start()
        TournamentTest.all_results[2] = results

        # Nick should always be last due to lower speed
        self.assertTrue(results[max(results.keys())] == "Nick")

    def test_tournament_usain_andrey_nick(self):
        tournament = Tournament(90)
        tournament.add_runner(self.runner1)
        tournament.add_runner(self.runner2)
        tournament.add_runner(self.runner3)

        results = tournament.start()
        TournamentTest.all_results[3] = results

        # Nick should always be last due to lower speed
        self.assertTrue(results[max(results.keys())] == "Nick")


if __name__ == '__main__':
    unittest.main()