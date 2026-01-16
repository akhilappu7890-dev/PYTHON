

item = input('enter a new item:')
file = open('shop.txt','a')
file.write(item + '\n')
file.close()


print('\nitem in the shop:')
file = open('shop.txt','r')
print(file.read())
file.close()
print('end')