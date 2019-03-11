from datetime import date

print('Amit')
d1 = date(1995,10,17)
d2 = date.today()
d3 = d2 - d1
print('Days passed from birth: '+str(d3.days))

d3 = date(d2.year, d1.month, d1.day)
d4 = d3 - d2
print('Days passed from this birthday: '+str(d4.days))

print('Pankaj')
d1 = date(1996,2,8)
d3 = d2 - d1
print('Days passed from birth: '+str(d3.days))

d3 = date(d2.year, d1.month, d1.day)
d4 = d3 - d2
print('Days passed from this birthday: '+str(d4.days)) 
