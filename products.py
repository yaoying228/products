import os     # operating system

products = []
if os.path.isfile('products.csv'):
    print('找到檔案了')
    with open('products.csv' , 'r' ) as f :
        for line in f :
            if '商品 , 價格' in line :
                continue                         #跳到下一回的意思
        name , price = line.strip().split(',')
        products.append([name , price])
    print(products)
        
else:
    print('沒找到檔案,可能遺失了..')

#輸入購買紀錄
while True:
    name = input('請輸入商品名稱:')
    if name =='quit':
        break
    price = input('商品價格:')
    price =int(price)
    p = []
    p.append(name)                   
    p.append(price)
    products.append(p)
print(products)

#印出購買紀錄
for p in products:
    print(p[0],'的價格是:',p[1])

#寫入檔案
with open('products.csv' , 'w') as f :
    f.write('商品 , 價格\n')
    for p in products:
        f.write(p[0] + ','+ str(p[1]) +'\n')      # price 轉換成整數了,所以要變為strip
