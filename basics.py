#         receiving input

# name = input("what's your name? ")
# print("hello" + " " + name)

''' number - 20
string - "chuj"
boolean - False'''

#converting types
'''
      jak chcemy cos dodac to musi byc ten sam typ wszystko i po to trzeba zmieniac o tako:
int() - converts value to an integer
str() - -,,- string
bool() - -,,- boolean
float() - -,,- float
'''

# birth_year = input("what is your birth year? ")
# age = 2022 - int(birth_year)
'''^tutaj sie uzywa int bo ten rok ktory wpisujemy na pytanie on traktuje jak string a nie ja numer a nie mozna odejmowac dwoch ruznych typow'''
# print("your age is " + str(age))
'''^ tutaj znowu przekonwertowac trzeba na stringa z powrotem'''

#      kalkulator dodajoncy dwie cyferki
# first_number = input("first number: ")
'''
# mozna tez zajebac floata tu od razu czyli first_number = input("first number: ")
'''
# second_number = input("second number: ")
# sum = float(first_number) + float(second_number)
# print("sum: " + str(sum))

#       stringi
sentence = "python for beginners"

# print(sentence.upper())

# print(sentence.replace('for', '4'))
'''^ tutaj jest 4 w '' bo ma byc stringiem bo for jest stringiem'''

# print(sentence.find('python'))

# print('python' in sentence)
'''^ on pyta czy w sentence jest python'''

#        arithmetic operators :3

# print(21 + 37)
# print(21 - 37)
# print(21 * 37)

'''two different types of division operators'''
# print(69 / 44)
'''^ dzieli normalnie i oddaje flołta'''
# print(69 // 44)
'''^ pisze ile razy 44 miesci sie w 69 bez przecinka czyli oddaje integer'''

# print(69 % 44)
'''^ modulus operator - returns the remainder of division 69 by 44'''

# print(69 ** 44)
'''this^ is an exponent operator and it returns 69 to the power of 44'''

'''      augmented assigment operator
        x = 10
        x = x + 3 to to samo co x += 3'''

#      comparison operators
'''
      > wieksze
      >= wieksze lub rowne
      < mniejsze
      <= mniejsze lub rowne
      == rowne
      != nierowne
'''

'''boolean true:'''
# x = 3 > 2
# print(x)

#        logical operators

'''
and - both
or - at least one
not - none
      'kao < 1' is called a boolean expression
'''
price = 25
# print(price > 20 and price <30)
'''^ and robi że jesli oba sa prawdziwe to bedzie true'''

# print(price > 20 or price < 30)
''' tu ^ jesli jedno albo drugie'''

#         if statements

# cat = int(input('what size is your cat? '))

# if cat > 30:
#   print('hell that is a long boi')
#   print('i bet he chunky!')
# elif cat > 20:
#   print('thats a medium gato')
# else:
#   print('he smol')
# '''indented stuff will be executed under conditions and not indented will be executed no matter what'''
# print("done!")
