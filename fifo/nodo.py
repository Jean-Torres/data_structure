class Nodo:
    def __init__(self, value) -> None:
        self.__value = value
        self.next = None

    def __str__(self) -> None:
        return str(self.__value)
