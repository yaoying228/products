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