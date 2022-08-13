end_list = open('result.txt','w') # 'w' creates file if doesn't existed
listdir = open('passive.txt')
order_set = [i.lower().replace(" ", "").strip() for i in open('active.txt').readlines()]

for line in listdir.readlines():
   if line.lower().replace(" ", "").strip() not in order_set:
       end_list.write(line)

