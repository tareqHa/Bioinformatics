import sys


s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] 
  
# using list comprehension 
listToStr = ' '.join(map(str, s)) 
  
print(listToStr)  

a, b, c = 1, 2, 3
print(max(a, b, c))
with open('config.txt') as myfile:
    all = myfile.read()
    print(all.strip(' \n,'))
    print('len = ', len(all.strip(' \n,')))
    sys.exit('FAILED')
