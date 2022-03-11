from NonDecorator import NonDecorator

class Driver:
    def main(self):
        # nd = NonDecorator()
        # amount = nd.net_price(2, 3)
        # print(amount)
        deco = NonDecorator()
        net_price = deco.currency()
        print(net_price(100, 0.05))
    if __name__ == '__main__':
        main(self='self')