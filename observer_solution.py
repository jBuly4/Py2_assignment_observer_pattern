from abc import ABC

class ObservableEngine:
    def subscribe(self, new_user):
        pass

    def unsubscribe(self, user):
        pass

    def notify(self, message):
        pass
