#mydict = {}
mydict = {'key1' : 'value1','key2': 'value2'}
print(mydict['key2'])
mydict['key3']= 'value3'
print(mydict)

d2 = {'key1': 'value1', 'key2': 123, 'key3' : 'value3', 'key4':{'123':[1,2,'findme']}}

print(d2['key4']['123'][2]) #оператор .upper делает буквы заглавными