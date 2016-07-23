a = 'Hello there!!!'
print '==> A ' + a

b=612
print '==> B ' + a + str(b)
print '==> C ' + a,str(b)
print '==> D ' + a,    str(b)

aa = ' Catch me if you can.... '
print '==> E ' + a+aa

bb = 388
print '==> F', b + bb
print '==> G ' + a + aa + 'I will give you $', b+bb, 'if you could... \nHehe...Just kidding\n'

print '==> H ' + a[3:]
print '==> I ' + a[0:4]
print '==> J ' + a[(len(a)-len(a)):((len(a)-len(a))+2)] + a[-14:-12]

print '==> K ' + a.lower()
print '==> L ' + a.upper()
print '==> M ' + a[0]
print '==> N '+a.replace('o','a')

print '==> O ' + a
print '==> P ' + aa.strip()
print '==> Q ' + aa

print '==> R ' + str(a.startswith('h'))
print '==> S ' + str(a.startswith('H'))

print '==> T ' + str(a.endswith('.'))
print '==> V ' + str(aa.endswith('.'))
print '==> W ' + str(aa.endswith(''))
print '==> X ' + str(aa.endswith(' '))

delimiter = ' '
print '==> Y',  aa.split(delimiter), '\n\n'

l = aa.split(delimiter)
print '==> Z',l,'\n'
print '==> 1 ' + ' '.join(l), '\n'
print '==> 2 ' + ''.join(l), '\n'
print '==> 3',l,'\n\n'

print aa

delimiter = ''
print aa.split(delimiter)
