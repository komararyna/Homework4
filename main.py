x=list(input('insert your number:'))
if 0 < len(x) < 5:
    el = int(x[0])
    el_2 = int(x[1])
    el_3 = int(x[2])
    el_4 = int(x[3])
    if el + el_2 == el_3 + el_4:
        print('Congratulations!Your number is lucky)')
    else:
        print('Your number isn`t lucky')
else:
    print('error')