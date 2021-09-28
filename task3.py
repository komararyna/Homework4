x = float(input('insert x:'))
y = float(input('insert y:'))
r = 4
hip = (x**2 + y**2) ** 0.5
if hip < r:
    print('ваша точка принадлежит кругу')
else:
    print('ваша точка не принадлежит кругу')