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
print '==> G ' + a + aa + 'I will give you $%d if you could... \nHehe...Just kidding\n'% (b+bb)

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
print '==> Y',  aa.split(delimiter)

l = aa.split(delimiter)
print '==> Z',l,'\n'
print '==> 1 ' + ' '.join(l) 
print '==> 2 ' + ''.join(l)
print '==> 3',l

print aa

ustr = u'A unicode \u018e string \xf1'
print ustr
s = ustr.encode('utf-8')
print s
print s==ustr
t = unicode(s,'utf-8')
print t==ustr

delimiter = ''
print aa.split(delimiter)
