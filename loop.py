cars = ['volvo', 'bmw', 'audi']
# for car in cars:
#     print(car)

# for car in range(len(cars)):
#     print(car)
    
# for index, car in enumerate(cars):
#     print (index, car)

for car in cars:
    if (car == 'volvo'):
        continue
    elif(car == 'audi'):
        break
    else:
        print('aloo')
    print(car)