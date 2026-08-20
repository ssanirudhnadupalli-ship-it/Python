from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

    def display_message(self):
        print("Message: Your order has been confirmed")


class EmailNotification(Notification):

    def send(self):
        print("Notification sent through Email")


obj = EmailNotification()
obj.send()
obj.display_message()