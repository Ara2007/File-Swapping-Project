#start = input("Shall we start?")

file1 = open("Sample1.txt","r")
data_a = file1.read()
print(data_a)

file2 = open("Sample2.txt","r")
data_b = file2.read()
print(data_b)

def swapFileData():

 with open("Sample1.txt", 'w') as a:
  a.write(data_b) 

with open("Sample2.txt", 'w') as b:
 b.write(data_a)

 print("Data swapped")





swapFileData()




