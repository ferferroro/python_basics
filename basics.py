# print function
# print('Magandang araw!')

# Variables
'''product = 'laptop'      # string
quantity = 50           # integer
price = 19999.99        # float
is_for_sale = True      # boolean True/False

print(product, quantity, price, is_for_sale)'''

product, quantity, price, is_for_sale = ('laptop', 50, 19999.99, False)

# print(product, quantity, price, is_for_sale)

# casting
price_integer = int(price)
'''print(price_integer, type(price_integer))
print(price, type(price))'''

# basic math
total_price = price * quantity
# print(total_price)

# concatenation - strings
'''print('I am selling ' + str(quantity) + ' ' + product + '(s) for ' + str(price) + ' pesos')
print(f'I am selling {quantity} {product}(s) for {total_price} pesos only!')'''

# List - collection ng data na ordered and changeable, can add duplicate (zero based)
'''list_numbers = [1,2,3]
list_numbers2 = list([1,2,3])
print(list_numbers, list_numbers2)'''

# create list
employee = ['cashier', 'supervisor', 'manager']
'''# change list value
employee[0] = 'two cashiers'
# access list value
print(employee[0])
# identify how many are there in the list
print(len(employee))
# append or add
employee.append('delivery man')
print(employee)
# remove
employee.remove('supervisor')
print(employee)
# insert - can specify what order
employee.insert(0,'accountant')
print(employee)'''

# Tuples - collection ng data na unordered at unchangeable
coordinates = (1,2)
# coordinates2 = tuple((3,5))
# print(coordinates, coordinates2)
# test accesing of tuple
# print(coordinates[0])
# test unchangeable
# coordinates.add(70)
# coordinates[0] = 5

# Set - collection ng data na unordered at unindexed, bawal yung duplicates
'''# set_1 = {1,2,3}
# set_2 = set({3,4,5})
# print(set_1, set_2)
tv_stations = {'abscbn', 'tv5', 'gma'}
print(tv_stations)
# add
tv_stations.add('myx')
print(tv_stations)
# remove
tv_stations.remove('gma')
print(tv_stations)
# test that we cannot add duplicate members
tv_stations.add('abscbn')
print(tv_stations)'''

# Dictionary -collection din ng data, ordered, changeable, indexed at no duplicates din
# para sya JSON 
# sample_dictionary = {
#     'name': 'rice cooker',
#     'price': 100
# }
# sample_dictionary2 = dict(name='electic fan', price=200)
# print(sample_dictionary, sample_dictionary2)

item = {
    'name': 'rice cooker',
    'price': 100
}

'''# accessing values
print(item['name'])

# add
item['color'] = 'white'

print(item)

# edit
item['price'] = 99

print(item)'''

# Function - block of code that will only run once you call it
def greetings(name='Guest'):
    print(f'Hello {name}!')

'''greetings()
greetings('Romel Fernando')'''

# Lamda Function - nameless function - this can take multiple inputs but can only execute one statement
'''getDiscountedPrice = lambda price, discount : price * (discount/100)

print(getDiscountedPrice(500,50))'''

# Conditionals - use to control flows ng program, base sa true or false statement
'''price = 85
payment = 85
if payment==0:
    print('Insufficient payment!')
# else if - eto yung next na mag execute pag nag fail sa unang condition
elif payment < price:
    print('Payment not enough!')
# else - catch! incase wala ni isang ma meet sa mga conditions sa taas
else:
    print('Payment is valid!')'''

# Logical operators - combine ng conditions [not, and, or]
'''price = 85
payment = 85
if payment==0:
    print('Insufficient payment!')
# else if - eto yung next na mag execute pag nag fail sa unang condition
elif payment < price:
    print('Payment not enough!')
# else - catch! incase wala ni isang ma meet sa mga conditions sa taas
else:
    # nested if
    # using logical operator 'or'
    change = payment - price
    if change != 0:
        print('Please wait for your change')
    # using logical operator 'and'
    if payment > price and change != 0:
        print(f'Your change is {change}!')
    # using logical operator 'or'
    if payment == price or change == 0:
        print('Thank you for giving the exact amount!')'''

# Loops - for iterations or set of code na uulit hangang ma reach yung certain condition
# For loops - mainly arrays or lists, tuples, sets or dictionary
# create list first
'''products = ['foods', 'drinks', 'clothes', 'toys']
# use of for loop
for product_offered in products:
    # using break will exit on the loop
    # if product_offered == 'drinks':
    #     break
    # using continue will skip
    if product_offered == 'foods':
        continue
    print(f'current produt: {product_offered}')'''

# While loop
'''loop_counter = 0
while loop_counter <= 5:
    # if loop_counter == 3:
    #     break
    loop_counter += 1

    if loop_counter == 2:
        continue

    print(f'current counter : {loop_counter}')'''

# while True:
#     print('forever loop')

# Modules - parang library na may useful na functions
# core modules - built in modules
'''import datetime
from datetime import date
from random import randrange

print(date.today(), randrange(1,10))

# pip modules - need to be installed
from camelcase import CamelCase
camel_case = CamelCase()
sample_string = 'this is a sentence that needs CamelCasing!'
print(camel_case.hump(sample_string))'''

# Clases at objects : class = blue print, object = object
'''class customer:
    # create constructor
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance

    # create function inside a class
    def get_summary(self):
        return f'Customer: {self.name} has {self.balance} balance!'

customer1 = customer('Romel Fernando', 500)

print(customer1.name, customer1.balance)
print(customer1.get_summary())'''

# Why?
# 1 - memorize syntax and grasp the fundamentals
# number na 1
# tagalog = isa
# english = one
# japanese = ichi

# 2. implement meaninful names in future projects
x = 1 # no idea para san yan
age = 1 # hindi ko pa ginagamit pero may idea na kao para san yan

# 3. create python app