from FullTimeEmployee import FullTimeEmployee
from HourlyEmployee import HourlyEmployee
from Payroll import Payroll

class Driver:
    def main(self):
        payroll = Payroll()

        payroll.__add__(FullTimeEmployee('Sandeep', 'Roy', 80))
        payroll.__add__(HourlyEmployee('Name', 'Surname', 30, 2))

        payroll.print()
    if __name__ == "__main__":
        main(self='self')