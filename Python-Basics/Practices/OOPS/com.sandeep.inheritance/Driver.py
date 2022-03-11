from BMW import BMW
from BMWConsumers import BMWConsumers
from MRacing import MRacing
class Driver:
    def main(self):
        x3 = BMW("Sedan", "x3", 2011, "Undefined")
        x3.showData()
        print()
        m3_consumer = BMWConsumers("Sedan", "M3", 2010, "Consumer", "E46")
        m3_consumer.showData()
        print()
        m3_racing = MRacing("GT-R", "M3 GTR", 2012, "Racing", "P60B40")
        m3_racing.showData()
    if __name__ == "__main__":
        main(self='self')