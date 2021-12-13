import os     # operating system

def read_file(filename):
    products = []
    with open(filename, 'r' ) as f :
        for line in f :
            if '商品 , 價格' in line :
                continue                         #跳到下一回的意思
            name , price = line.strip().split(',')
            products.append([name , price])
        return products
      
#輸入購買紀錄

def use_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if name =='q':
            break
        price = input('商品價格:')
        price =int(price)
        p = []
        p.append(name)                   
        p.append(price)
        products.append(p)
    print(products)
    return products

#印出購買紀錄

def print_products(products):
    for p in products:
        print(p[0],'的價格是:',p[1])

#寫入檔案

def write_file(filename,products):
    with open(filename , 'w' ) as f :
        f.write('商品 , 價格\n')
        for p in products:
            f.write(p[0] + ','+ str(p[1]) +'\n')      # price 轉換成整數了,所以要變為strip

def main():
    filename= 'products.csv'
    if os.path.isfile(filename):
        print('太棒了!找到檔案囉')
        products = read_file(filename)
    else:
        print('沒找到檔案,可能遺失了..')
    products = use_input(products)
    print_products(products)
    write_file('products.csv',products)

main()
