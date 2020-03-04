# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list()
b = list()
c = list()
d = list()
x = str(input())
for i in x:
    if i.islower():
        a.append(i)
    if i.isupper():
        b.append(i)
    if i.isnumeric() and int(i) % 2 != 0:
        c.append(i)
    if i.isnumeric() and int(i) % 2 == 0:
        d.append(i)
a.sort()
b.sort()
c.sort()
d.sort()
a = ('').join(a)
b = ('').join(b)
c = ('').join(c)
d = ('').join(d)
print(a + b + c + d)

