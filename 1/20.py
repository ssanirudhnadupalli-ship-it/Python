from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self):
        pass

    def display_report_info(self):
        print("Report: Monthly Sales Report")


class SalesReport(Report):

    def generate(self):
        print("Monthly sales report generated")


obj = SalesReport()
obj.generate()
obj.display_report_info()