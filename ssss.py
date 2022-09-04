#scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
#a,b,*valid_score = scores

#print(*valid_score)

#scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
#a, *valid_score, b = scores
#print(valid_score)

#temp = {}

#dict = {"메로나":1000,"폴라포":1200,"빵빠레":1800,"죠스바":1200,"월드콘":1500}

#print(dict['메로나'])

#ice = {'메로나': 1000,
#       '폴로포': 1200,
#       '빵빠레': 1800,
#       '죠스바': 1200,
#       '월드콘': 1500}
#del ice['메로나']

#print(ice)
#icecream = {'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}

inventory = {"메로나": [300, 20],"비비빅": [400, 3],"죠스바": [250, 100]}



inventory['월드콘']=[500,7]

print(inventory['메로나'][1])


icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

d1 = list(icecream.values())
print(sum(d1))

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}


icecream.update(new_product)
print(icecream)

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys,vals))
print(result)


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date,close_price))
print(close_table)
