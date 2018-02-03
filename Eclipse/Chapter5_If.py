cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
requested_topping='dat pussy'
if requested_topping != 'anchovies':
    print("Hold the anchovies !")
requested_topping=['pineapple','peporoni','black olives']
if 'bannana peppers' not in requested_topping:
    print("Would you like to add bannana peppers?")
else:
    print("Thank you for your order!")
## or I could use requested_toppings.append
requested_topping.insert(2, 'bannana peppers')
if 'bannana peppers' not in requested_topping:
    print("Would you like to add bannana peppers?")
else:
    print("Thank you for your order!")
age=12
if age<4:
    print("Your admission cost is free)")
elif age<18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
## Or a cleaner way would be to set the price in the if statement and then just have on print 
age=24
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
else:
    price=7
print("The price of your admission is $"+str(price)+' bitches!')

requested_topping=['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
    print('Adding mushrooms.')
if 'pepperoni' in requested_topping:
    print('Adding pepperoni')
if 'extra cheese' in requested_topping:
    print('Adding extra cheese')
print('\nFinished making your pizza!')
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print('Adding '+requested_topping.title()+'.')

print("\nFinished making your pizza")

available_toppings=['mushrooms','olives','green peppers','pepperoni','pinapple','extra cheese']
requested_toppings=['mushrooms','french fires','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding '+requested_topping.title()+' to your pizza')
    else:
        print("I am sorry we don't have "+requested_topping.title()+',')
print("\nWe have finsihed making your pizza")

    