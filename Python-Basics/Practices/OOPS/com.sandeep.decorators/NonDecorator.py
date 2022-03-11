class NonDecorator:
    def net_price(self, amount, tax):
        result = amount * (1 + tax)
        return result
    def currency(net_price):
        def wrapper(*args, **kwargs):
            result = net_price(*args, **kwargs)
            return f'${result}'
        return wrapper