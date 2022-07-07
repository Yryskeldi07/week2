#print(23*56/165)
#print(1/55+2**12)

#Enterword1 = input('Enter word:')
#Enterword2 = 'False'
#Ispalinbol1 = input('Is palindrom:')
#Ispalinbol2 = int('True')
#print(Enterword1 == Enterword2 and Ispalinbol1 == Ispalinbol2)
#word = input('Enter a word:')
#print('Is palindrom:', word ==word{::-1})

#print('**********')
#print('**********')
#print('**********')
#print('**********

#list список колекции
#a = [1, 2, 3, 4]
#lists = [1, 'kdndfn', 2.3, [1,2], {'s':3}, ]
#str_1 = 'hello world'
#print(lists[3])
#for i in range(10, 15, 2):
#    print(i)
   # print('len = ', len(lists))


#for i in range(0, 101,2 ):
#print(i)
#lists_1 = list(range(0, 101,2 ))

#lists_1 = list('str')
#print(lists_1)

#append()
#lists = [1, 'nazgyl', 2.3, [1,2], {'s':3}, ]
#len(lists)
#lists.append({'name': 'nazgyl'})
#lists.append([1, 3, ])
#lists.extend([1, 3, ])
#print(lists[1], 'before')
#lists.insert(1, 5)
#print(lists[1], 'after')
#print(lists)



#phone_numbers = [
 #                '+996709372927',
#                 '+996554928378',
#                 '+996567898765',
#                '+996567898765',
#               ]
#black_list = phone_numbers.pop(2)
#print(black_list)
#print(phone_numbers)
#phone_numbers.insert(2, black_list)
#print(phone_numbers)

#phone_numbers.remove('+996567898765')
#print(phone_numbers.count('+996567898765'))
#phone_numbers.reverse()
#print(phone_numbers)

#start = int(input('start '))
#end = int(input('end '))
#step = int(input('step '))
#power = int(input('power '))

#lists = []
#for i in range(start, end, step,):
 #   lists.append(i**power)
 #   print(lists)
#lists.clear()
#print(lists)

#empty = [1, 4, 3, 2]
#empty.sort()
#               print(empty)


#print(3)


#a = [1, 3, 4]
#s = 'String'
#a.reverse()
#s.lower()
#print(a)
#print(s.lower())





# if
#num1 = int(input('num1: '))
#num2 = int(input('num2: '))
#operator = input('operator: ')
#if operator == '+':
  #  result = num2 + num1
 #   print('result = {}'.format(result))


#elif operator == '-':
  #  result = num1 - num2
 #   print('result = {}'.format(result))

#elif operator == '*':
    #    result = num1 * num2
   #     print('result = {}'.format(result))


#elif operator == '/':
 #   result = num1 / num2
  #  print('result = {}'.format(result))


#if num1 > num2:
#    print('{0} grater {1}'.format(num1, num2))
#elif num2 > num1:
#    print('{0} grater {1}'.format(num2, num1))




#lists = [1, 2]
#lists = [1, 2, 3, 4]



#if 3 in lists:
 #   print('hello')


#or and


#lists = [18, 22, 25, 6]
#if 22 in lists and 25 in lists:
#    print('yes')


#for i in range (0, 1001) :
 #   if i % 5 == 0:
#print(i)

#s = 0
#for i in range(0,1000):
 #   if i % 15 == 0:
  #      s += i
   #print(s)



#nums = [3, 5, 15]
#max = 1001

##for num in range(1,max):
  #  if num*i < max:
   #     result += num*i
#print(result)

#result = []
#for i in range(0,max):
 #   if i%3 == 0 and i%5 == 0 and i%15 == 0:
  #      result.append(i)
#print(result)



#temp = int(input('vedite temp: '))
#operator = input('C or F ? : ')
#if operator == 'C':
#    result = 5/9*(temp-32)
##    print('v far = {}'.format(result))
##elif operator == 'F' :
#    result = 9/5*(temp+32)
#print('v cel = {}'.format(result))



#s1=int(input())
#for i in range(s1):
#    print(i +1, end='\t')
#    for g in range(i):
 #print((g+1)*i


#from random import randint
#print(randint(1, 10))

#from  random import randint


#for i in range(1, 11):
#    n1 = randint(1, 10)
#    n2 = randint(1, 10)
#    result = int(input(f'Question {i}: {n1} * {n2}  ='))
#    if result == n1 * n2:
#        print('Right!')
#    else:
#print(f'Wrong. The answer is {n1 * n2}')



#from  random import randint

#for i in range(1, 13):
#    am = randint(1, 12)
#    pm = randint(1, 12)
#   result = int(input(f'How many hours ahead? :'))
#    Newhour =



#tuple



#tuples = (1, 2, 3)
#for i in tuples:
#    print(i+2)
#print(tuples[2])
#for i in ran

#tuples1 = tuples()
#tuples2 = (1,)
#print(type(tuples2))


#print(len(tuples))


#dictionary


#dict1['name2'] = 'yasir'
#dict_2["name1"] = 'yrs'
#print(dict_1)
#print(dict_1['name1'])


#items()

#for i in dict_1.items():
 #   print(i)

#values

#for i in dict_1.values():
 #   print(i)



#keys()
#for i in dict_1.keys():
 #   print(i)


#print(type(dict_1.keys))
#print(dict1.values())


#dict = {
 #   'name1': ['Nazgul', 'Vadim'],
  #  'name2': 'Mirlan',
   # 'name3': 'Andrey',
#}



#students = {
 #   'Ulan': 98,
  #  'Kunduz': 90,
   # 'vadim': 99,
    #'Nurdin': 100
#}
#summ = sum(students.values())
#result = sum(students.values()) / len(students)
#print(result)




#update
#after_exam = {}

#for key, values in students.items():
   # print(key, values)
 #   val = values - 2
  #  after_exam.update(
   #     {key: val}
#    )


#print(after_exam)


#other = {
  #  'Tannuru':88,
 #   'azamat':78,
#}

#students.update((other))
#print(students)


#fromkeys


#lists = ['book1', 'table', 'board']
#dicts = dict.fromkeys(lists, 20)
#print(dicts)
#dicts.clear()
#print(dicts)



#dicts_1 = dicts.copy()
#print(dicts_1)



#other = {
 #  'Tannuru': 88,
  #  'Azamat': 78



#products ={}
#product_name = 'Albeni'
#product_price = 40
#products[product_name] = product_price

#print(products)


#profile ={}

#for i in range(2):
 #   product_name = input('Enter product name: ')
  #  product_price = input('Enter product price: ')
   # products[product_name] = product_price



#search_value = input('Enter product name: ')
#if search_value in products.keys:
#    print(f'Product name: {search_value}, price: {products[search_value]}')
#else:
 #   print('Not found')

# min_value = int(input('Enter price: '))
 #for key, value in products.items():
  #   if value < min_value:
   #      print(f'Product name: {key}, price: {value}')


#
#print(other.get('Yryskeldi', True))
#print(other['d'])


#print(other)

#removed = other.pop('Tannuru')
#removed = other.popitem()
#print(removed)
#removed2 = other.popitem()
#print(removed2)
#(other.setdefault('Aza', 86))
#other[removed2[0]] = removed2[1]
#print(other)

#students = {
#    'Andrei':{
#        'int':50,
#        'str':77,
#        'if':90
#    },
#    'Mirlan': {
#        'int':50,
#        'str':78,
#        'if':90
#    },
#    'Yasir': {
#        'int': 80,
#        'str': 82,
#        'if': 87
#    },
#    'Aidar': {
  #      'int':99,
 #       'str':95,
  #      'if':98
 #   },
#    'Bekbolsun': {
  #      'int':65,
 #       'str':67,
 #       'if':66
#    }
#}
#avg = {}
#for i in students:
    #val = sum(students[i].values()) / len(students[i].values())
    #avg.update(
    #  {
   #       i: val
  #    }
 # )
#print(avg)
   # print(sum(students[i].values()))




#i = 0
#while i<10:
#   print(i)
 #    i += 1



#while True:
#    i = input('Vvedite chislo: ')
#    if i.lower() == 'stop':
#        print('BYE BYE')
#        break


#while True:
#    print('Hello world')


#y = 0
#while y < 4:
#    t = input('Vvedite password: ')
#    y += 1
#    if t!='2003':
#        print('Nepravilnyi parol ostaloc popytok :', 4-y)
#        print('Vy udaleny iz sistemy')
#    else:
#        print('Vy udaleny iz sistemy')
#        break

#cities = ['Bishkek', 'Tashkent', 'NEW York', 'paris', 'moskow']
#x = ['x'] * len(cities)
#print(''.join(x))
#while True:
#    symbol = input('Введите букву: ').upper()
#    for i in range(len(cities)):
#        if cities[i] == symbol:
#            x[i] = symbol
#    s = ''.join(x)
#    print(s)
#    if s == cities:
#        break

#while True:
 #   user = input('VVedite bykvy ili nazovite slovo')
  #  if user == cities:
#        print('Vy vvely pravilno');break
#    if (user in cities):
#            print ('est takaia bykva')
#            for i in range (0, len(cities)):
#                if cities[i] == user:
#                    curent_view[i]=user
#                    user_cities=''.join(curent_view)
 #   else:
 #       print('takoi bykvy net')
#    if user_cities == cities:
#        print('vy pravilno nazvali vce bykvy');break

#    print(user_cities)

# set - mnojestvo
#set1 = {1, 'Ulan', 2, 3, 4, 1}
#print(set1)



#set1 = set()
#print(type(set1))


#for i in set1
#    for j in i:
#        print(j)


#union



#set1 = {'monday', 'thusday', 'wednesday', 'saturday'}
#set2 = ({'saturday', 'friday', 'monday'})
#s  = set1.union(set2)
#set1.add('saturday')
#set1.clear()
#set2.symmetric_difference_update(set1)
#print(set2)

#str1 = {'a', 'b', 'c'}
#str2 = {'a', 'b', 'd'}
#str_set = str1.difference(str2)
#str1.difference_update(str2)
#print(str1)
#pop_set = str1.pop()
#print(pop_set)


#str2.discard('x')
#str2.remove('a')
#print(str2)
#print(str1)


#a = [1, 2, 3, 4, 6, 7, 8, 9, 9]
#b = [6, 1, 5, 6, 7, 9 ]


#a1 = set(a)
#b1 = set(b)
#print(a1.issubset(b1))
##a1.intersection_update(b1)
#print(a1)

#a1 = set(a)
#a2 = list(a1)
#print(a2)
#print(a1.issuperset(b1))




#set1 = {
#    1, 2, 3, 4, 5
#}

#set2 = {
 #}

#set1.update(set2)

#print(set1.union(set2))
#print(set1)


#set1 = {'Hello ', 'banana'}
#set2 = {'Hello', 'apple', 'pineapple'}
#set3 = {'Hello', 'potato', 'orange'}
#print(set1.intersection(set3, set2))
#set1.update(set2)
#print(set1.union(set2))


#print(set1.isdisjoint(set2))





#set1 = {3, 2, 6, 7, 8, 4, 5}
#set2 = {6, 9, 8, 1, 2, 3}
#set1.intersection_update(set2)
#print(set1.intersection(set3, set2))
#print(set1)
#print(set1.intersection(set2))
#set1.update(set2)
#print(set1.union(set2))


#set1 = {1, 2}
#set2 = {3}
#set3 = {4, 5}
#set4 = {3, 2, 6}
#set5 = {6}
#set6 = {7, 8}
#set7 = {9, 8}
#set1.update(set2, set3, set4, set5, set6, set7)
#set1.intersection(set2, set3, set4, set5, set6, set7)
#set1.update(set2, set3, set4, set5, set6, set7)
#set1.update(set2, set3, set4, set5, set6, set7)
#set1.intersection_update(set2, set3, set4, set5, set6, set7)
#print(set1)

#x = {3, 5, 2}
#y = {3, 5, 2, 6}

#if x.issuperset(y):
#    print('eto supermnogestvo')

#else:
#    print('eto ne super mnogestvo')

#if x == y:
#    print('oni ravny')



#comprehentions - lists, dict



#lists = []
#for i in range(1, 10000000):
#    lists.append(i)

#print(lists)


#lists = [i for i in range(1, 10000001)]
#print(lists)



#import datetime


#time_now = datetime.datetime.now()
#print(time_now)

#lists = []
#for i in range(1, 10001):
#    lists.append(i)
#delta = datetime.datetime.now() - time_now
#print(delta)




#time_now = datetime.datetime.now()
#lists = [i for i in range(1, 10001)]
#delta = datetime.datetime.now() - time_now
#print(delta)



#lists = [i**2 for i in range(1, 10001) if i % 2 == 0 and i % 5 == 0]
#print(lists)


#number = int(input())
#fact = 1
#for i in range(1, number + 1):
#    fact *= i
#print(fact)c


#dicts = {i: i**2 for i in range(1, 5)}
#rint(dicts)


#lists = [i for i in range(1, 10000001)]
#print(lists)


#lisst = {i: i*2 for i in ['applee', 'banana']}
#print(lisst)

import random
#ver = 0
#while (ver == 0):
#        player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
#        if (player == 1 or player == 2 or player == 3):
#            ver = 1
#if player == 1:
#       print("Вы выбрали камень.")
#if player == 2:
#        print("Вы выбрали ножницы.")
#if player == 3:
#        print("Вы выбрали бумагу.")
#comp = random.randint(1, 3)
#if comp == 1:
#        print("Компьютер выбрал камень.")
#if comp == 2:
#        print("Компьютер выбрал ножницы.")
#if comp == 3:
#        print("Компьютер выбрал бумагу.")
# определяем победителя
#if player == comp:

#        win = 0
#if player == 1 and comp == 2:
#        win = 1
#if player == 1 and comp == 3:
#        win = 2
#if player == 2 and comp == 1:
#        win = 2
#if player == 2 and comp == 3:
#        win = 1
#if player == 3 and comp == 1:
#        win = 1
#if player == 3 and comp == 2:
#        win = 2
#if win == 0:
#        print("Ничья!")
#if win == 1:
#        print("Победил игрок!")
#if win == 2:
#        print("Победил компьютер!")





#def determine_winner(user_action, computer_action):
#    if user_action == computer_action:
#        print(f"Оба пользователя выбрали {user_action.name}. Ничья!")
#    elif user_action == Action.Rock:
#        if computer_action == Action.Scissors:
#            print("Камень бьет ножницы! Вы победили!")
#        else:
#            print("Бумага оборачивает камень! Вы проиграли.")
#    elif user_action == Action.Paper:
#        if computer_action == Action.Rock:
#            print("Бумага оборачивает камень! Вы победили!")
#        else:
#            print("Ножницы режут бумагу! Вы проиграли.")
 #   elif user_action == Action.Scissors:
 #       if computer_action == Action.Paper:
 #           print("Ножницы режут бумагу! Вы победили!")
 ##       else:
 #           print("Камень бьет ножницы! Вы проиграли.")


#import random


#start = input('Вы запустили игру "Камень, ножницы, бумага". Хотите поиграть? (Вводите + или -): ')

##if start == '+':
#    print('Загрузка...')
#    print("Загрузка завершена! Начинаем!")
#    print("3...2...1...")
#    print('Если захотите закончить вводите "-".')
#    print('Если захотите узнать счёт вводите "с".')
#    user_ball = 0
#    rand_ball = 0
#    while True:
#        user = input("Камень, ножницы или бумага? (Вводите к, н или б): ")
#list_play = ['к', 'н', 'б']
##        if user in list_play:
#            rand = random.choice(list_play)
#            print(rand)

#            if rand == 'к' and user == 'н':
#                rand_ball += 1
#            if rand == 'к' and user == 'б':
#                user_ball += 1
#            if rand == 'н' and user == 'к':
#3                user_ball += 1
 #           if rand == 'н' and user == 'б':
#                rand_ball += 1
#            if rand == 'б' and user == 'н':
#                user_ball += 1
#            if rand == 'б' and user == 'к':
#                rand_ball += 1
#        elif user == 'с':
#            print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")









#summ = int(input('summ: '))
#year = int(input('year: '))
#precent = float(input('precent '))

#def get_cash(summ, year, precent):
#    precent_one_year = summ * precent
#    all_cash = precent_one_year * year + summ
#    print(all_cash)
#    return  all_cash

#print(get_cash((10000, 5, 0.2)))
#print(get_cash((12000, 5, 0.2)))
#print(get_cash((11000, 5, 0.2)))

#start = int(input("Начальная сумма = "))
#year = int(input("ГОДЫ = "))
#percent = (0.1)

#def get_cash(start, year, precent=0.1):
#    precent_one_year = start * precent

#    all_cash = precent_one_year * year + start
#    print(all_cash)
#    return all_cash
#    posle = all_cash * precent
#    print(posle)
#cur = start
#q = 1 + percent / 100
#d = 1
#while cur < year:
#    d += 1
#print(d - 1)



#def get_cash(summ, year, precent):
#    precent_one_year = summ * precent
#    all_cash = precent_one_year * year + summ
#return  all_cash






#from sys import argv

#first = argv[1]
#second = argv[2]
#print('second')


#shop_cash = [10000, 34000, 30000, 12300, 45000, 90000, 78999]
#expenses = [1000, 3000, 20000, 5000, 5600, 7654, 3425]
#all_cash = sum(shop_cash)
#all_expenses = sum(expenses)
#profit = all_cash - all_expenses
#print(profit)

#shop_cash2 = [10000, 34200, 30000, 12300, 45000, 90000, 78999]
#expenses2 = [102000, 30020, 20000, 500, 5600, 7654, 3425]


#def get_many(shop_cash: list,  expenses: list):
#    all_cash = sum(shop_cash)
#    all_expenses = sum(expenses)
#    profit = all_cash - all_expenses
#    return profit


#monday = get_many(shop_cash, expenses)
#day2 = get_many(expenses=expenses2, shop_cash=shop_cash2)
#print(day2)


#*args **kwargs


#def get_argumets(*args, **kwargs):
#    if args:
#        print(args)
#    if kwargs:
#        print(kwargs)


#get_argumets(1, 2, 3, 'dffgg', {1, 0}, name='Nazgul', age=26)



#d = {'name: 'Nazgul',
#      'age: 26'}



def get_list_square(*args, **kwargs):
    result = []
    if args:
        for i in args:
            result.append(i**2)
    if kwargs:
        for key, value in kwargs.items():
            if type(value) == str:
                kwargs.update({
                    key: value.upper()
                })
            if type(value) == set:
                kwargs.update({
                    key: [value]
                })


    return result, kwargs

print(get_list_square(1, 3,7, 11, name='nazi', age=50, sets={1, 3}))






#    return result
#print(get_list_square(1, 3, 7, 11))

























