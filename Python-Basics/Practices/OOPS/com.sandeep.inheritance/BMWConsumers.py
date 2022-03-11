from BMW import BMW
class BMWConsumers(BMW):
    engine_variant = ''
    def __init__(self, fleet, model, year, lob, engine_variant):
        super(BMWConsumers, self).__init__(fleet, model, year, lob)
        self.engine_variant = engine_variant
    def showData(self):
        print("Self: ", self.fleet)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print("LOB: ", self.lob)
        print("Engine Variant: ", self.engine_variant)


