# runner.py
class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError(f"Имя может быть только строкой, передано {type(name).__name__}")
        if speed < 0:
            raise ValueError(f"Скорость не может быть отрицательной, сейчас {speed}")
        self.name = name
        self.speed = speed
        self.distance = 0

    def run(self):
        self.distance += self.speed

    def __eq__(self, other):
        return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
