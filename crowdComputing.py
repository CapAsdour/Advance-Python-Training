n=[100,200,524,321,526,145,521,789,256,325,652,149,555]
n.sort();
print(n)
a=len(n)
s=0
b=round(.1*a)
for i in range(b,a-b):
    s+=n[i]
    print(s)    
print(s/(a-2*b))    