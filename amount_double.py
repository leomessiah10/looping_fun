print('This program evlautes the time by which \n'
      'the principle amount will get doubled')

amount,rate = eval(input('Enter the amount, interest rate '))
temp = amount
count = 0

while(True):
    amount = amount * (1 + rate)
    count += 1
    if amount == temp*2:
        break
    else:
        continue


print('The amount got doubled in {} years'.format(count))
