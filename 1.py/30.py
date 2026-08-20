from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def authenticate(self):
        pass


class Password(Authentication):
    def authenticate(self):
        print("Authenticated using Password")


class OTP(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class GoogleLogin(Authentication):
    def authenticate(self):
        print("Authenticated using Google Login")


class Biometric(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")


Password().authenticate()
OTP().authenticate()
GoogleLogin().authenticate()
Biometric().authenticate()