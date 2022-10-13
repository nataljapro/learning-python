weight = float(input('what is your cats weight? :3 '))
unit = input("in (k)g or (l)bs? ")
if unit == 'k':
  print('thats ' +  str((weight * 2.2)) + 'lbs ')
if unit == 'l':
  print('thats ' +  str((weight * 0.45)) + 'kg ')
print('oki bye')