from abc import ABC, abstractmethod

class CloudStorage(ABC):

    @abstractmethod
    def upload(self, file):
        pass


class GoogleDrive(CloudStorage):
    def upload(self, file):
        print(file, "uploaded to Google Drive")


class AWSStorage(CloudStorage):
    def upload(self, file):
        print(file, "uploaded to AWS Storage")


class AzureStorage(CloudStorage):
    def upload(self, file):
        print(file, "uploaded to Azure Storage")


GoogleDrive().upload("document.pdf")
AWSStorage().upload("image.jpg")
AzureStorage().upload("video.mp4")