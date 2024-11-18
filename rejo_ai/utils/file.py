from abc import ABC


class File(ABC):
    @staticmethod
    def create_pdf(name:str):
        print("file created successfully....")