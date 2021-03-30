keep_going = 'y'

while keep_going == 'y':
    temp = float(input('Enter temperature in degrees Celsius:'))
    print('Turn down the temperature, wait 5 minutes, check again')
    keep_going = input('Is the temperature greater than 102.5?' '(Enter y for yes): ')
    print('Check temperature again in 15 minutes')
    
