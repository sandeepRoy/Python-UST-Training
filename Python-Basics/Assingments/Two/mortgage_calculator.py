def monthly_payment_calculate(months, rate, loan):
    monthly_rate = rate / 100 / 12
    monthly_payment = (monthly_rate / (1 - (1 + monthly_rate) ** (-months))) * loan
    return monthly_payment

def compounded_amount_calculate(months, rate, loan):
    choose_compounding_interval = input("Compounding Interval: Daily/ Weekly/ Monthly/ Continually: ")
    if (choose_compounding_interval == 'Daily'):
        amount = loan * (pow((1 + rate / 100), 1))
    elif (choose_compounding_interval == 'Weekly'):
        amount = loan * (pow((1 + rate / 100), 7))
    elif (choose_compounding_interval == 'Monthly'):
        amount = loan * (pow((1 + rate / 100), 30))
    else:
        amount = loan * (pow((1 + rate / 100), months))
    compound = amount - loan
    return compound

if __name__ == "__main__":
    months = int(input("Enter mortgage term (in months): "))
    rate = float(input("Enter interest rate: "))
    loan = float(input("Enter loan value: "))
    compound = 0

    monthly_payment = monthly_payment_calculate(months, rate, loan)
    print(monthly_payment)

    compounded_amount = compounded_amount_calculate(months, rate, loan)
    print(compounded_amount)