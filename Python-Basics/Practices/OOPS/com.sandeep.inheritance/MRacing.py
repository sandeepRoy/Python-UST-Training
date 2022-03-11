from BMW import BMW
class MRacing(BMW):
    engine_build = ''
    def __init__(self, fleet, model, year, lob, engine_build):
        super(MRacing, self).__init__(fleet, model, year, lob)
        self.engine_build = engine_build
    def showData(self):
        print("Self: ", self.fleet)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print("LOB: ", self.lob)
        print("Engine Build: ", self.engine_build)
