car_name = input('enter car name:')
buying_price = float(input('enter buying price:'))
repair_cost = float(input('enter repair (booving) cost: '))
other_cost = float(input('enter other cost: '))
selling_price = float(input('enter selling price: '))

total_cost =buying_price + repair_cost + other_cost
profit = selling_price - total_cost

print('\n--- RESULT ---')
print('car:', car_name)
print('total cost:', total_cost)
print('selling price:', selling_price)
if profit > 0:
    print('profit', profit, '+')
elif profit < 0:
    print('loss:', profit, '-')
else:
    print('no profit, no loss')

car_name: input('toyota camry')
buying_price: input('200000')
repair_cost : input('5000')
other_expenses: input('10000')
selling_price: input('5000')

car_name: input('benz')
buying_price: input('120000')
repair_cost: input('5000')
other_expenses: input('1000')
selling_price: input('500000')

car_name: input('rx350')
buying_price: input('10000')
repair_cost: input('2500')
other_expenses: input('1200')
selling_price: input('13000')

car_name: input('gwagon')
buying_price: input('5')
repair_cost: input('4')
other_expenses: input('6')
selling_price: input('9')

car_name: input('golf')
buying_price: input('20')
repair_cost: input('2')
other_expenses: input('3')
selling_price: input('4')

car_name: input('sharon')
buying_price: input('5')
repair_cost: input('2')
other_expenses: input('2')
selling_price: input('10')





