#Count frequency of words 

text = "here i teach you python code easy and frequently ...."

list = text.split()
dict = {}
print(list)
for i in list:
    if i not in dict:
        dict[i] =1
    else:
        dict[i] +=1
        
print(dict)
