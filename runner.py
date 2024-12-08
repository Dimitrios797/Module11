class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError(f"Имя может быть только строкой, передано {type(name).__name__}")
        if speed < 0:
            raise ValueError(f"Скорость не может быть отрицательной, сейчас {speed}")
        self.name = name
        self.speed = speed