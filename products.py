products = []
while True:
    name = input('請輸入商品名稱:')
    if name =='quit':
        break
    price = input('商品價格:')
    p = []
    p.append(name)                   #No.7~10 可簡化為 produtcts.append([name , price])
    p.append(price)
    products.append(p)
print(products)

for p in products:
    print(p[0],'的價格是:',p[1])

with open('products.csv' , 'w') as f :
    for p in products:
	    f.write(p[0] + ','+ p[1] +'\n')
f.write()