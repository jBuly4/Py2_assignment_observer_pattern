from abc import ABC

class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, new_user):
        self.__subscribers.add(new_user)

    def unsubscribe(self, user):
        self.__subscribers.remove(user)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achivement):
        self.achievements.add(achivement['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, achivement):
        if achivement not in self.achievements:
            self.achievements.append(achivement)
