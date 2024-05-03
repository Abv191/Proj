from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def get_input(self, prompt):
        pass

class ConsoleUserInterface(UserInterface):
    def display_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt).strip().lower()
