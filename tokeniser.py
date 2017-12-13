# -*- coding: utf-8 -*-

#Class 3
text = "example of text";
tokens=text.split( )
print(tokens)

l=[]
for i in range(len(tokens)):
    l1=['-']*8
    l2=[i,tokens[i]]
    l.append(l2+l1 )
print(l)

l[0][4]="NOUN";
l[1][4]="ADV";
l[2][4]="NOUN";

print(l)



