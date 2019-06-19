from PIL import Image
from collections import Counter

s = "C:/Users/omtha/Downloads/Final Submission/JPEG File/fax.jpg"

im=Image.open(s).convert('L')
data=list(im.getdata())
counts=Counter(data)
l=[str(i)+'\n' for i in data]
l.append(str(im.size))
open('test1.txt','w').writelines(l)
f=open('test2.txt','w')
data=list(set(data))
for i in data:
    f.write(str(i)+','+str(counts[i])+'\n')