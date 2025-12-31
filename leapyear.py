year=int(input('Enter a number'))
if year%4==0 and year%100!=0 or year%400==0 :
    print("entered year is a Leap Year")
else:
    print('entered year is not a Leap Year')