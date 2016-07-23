
colors = ['red', 'blue', 'green']
print colors[0]
print colors[2]
print len(colors)

b = colors ## Does not copy the list
c = colors[:]
b[0] = 'Yellow' #Let us try, check
print 'I altered assigned, now printing got assigned\n', colors
### Then how can we copy the list!!!
## let us try , atfer this i wrote  c = colors[:]
print c ## Now try printing c, What we can see??? 

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
	sum += num
print sum

list = ['Jingle', 'Bells', 'Merry', 'Christmas']
if 'Bells' in list:
	print 'yay'

list[0]='Hihi Jingle'
print list

list.append(['Holidyas...', 'Holidays...'])
list.extend(['After then', 'soon be', 'New Year', ' !!!'])
list.insert(0,'Dec')
print list

print list.index('Christmas')
list.remove('New Year')
print list
print list.pop()
print list + ['Again!!!']
print list.pop(0)

print list[2:-1]
list[-3:-2] = ['Holidays!!!']
list.pop()
print list

