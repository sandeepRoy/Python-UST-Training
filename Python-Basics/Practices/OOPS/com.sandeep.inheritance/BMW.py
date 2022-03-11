class BMW:
    def __init__(self, fleet, model, year, lob):
        self.fleet = fleet
        self.model = model
        self.year = year
        self.lob = lob

    def showData(self):
        print("Fleet: ", self.fleet)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print("LOB: ", self.lob)
