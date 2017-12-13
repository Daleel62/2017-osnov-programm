# -*- coding: utf-8 -*-

#transliteration table 



table=[["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"], ["a","b","v","g","d","e","ë","zh","z","i","ĭ","k","l","m","n","o","p","r","s","t","u","f","kh","ts","ch","sh","shch","ʺ","y" ,"ʹ","ė" ,"you","ya"]]

text="бдж кл"
tokens=text.split( )
print(tokens)

l=[]
for i in range(len(tokens)):
    l1=['-']*8
    l2=[i,tokens[i]]
    l.append(l2+l1 )

print(l)

translit=[]
for i in range(len(l)):
    l1=[]
    for j in range(len(l[i][1])):
        n=table[0].index(l[i][1][j]);
        l1.append(table[1][n]);
    translit.append(l1)

print(translit)

text2="Это течение следует на север до Японского побережья, оказывая заметное влияние на климат японского побережья"
tokens2=text2.split( )
print(tokens2)


li=[]
for i in range(len(tokens2)):
    l1=['-']*8
    l2=[i,tokens2[i]]
    li.append(l2+l1 )

li[0][4]="DET";
li[1][4]="NOUN";
li[2][4]="VERB";
li[3][4]="ADP";
li[4][4]="NOUN";
li[5][4]="ADP";
li[6][4]="ADJ";
li[7][4]="NOUN";
li[8][4]="PUNC";
li[9][4]="VERB";
li[10][4]="ADJ";
li[11][4]="NOUN";
li[12][4]="ADP";
li[13][4]="NOUN";
li[14][4]="ADJ";
print(li)


uni=["VERB","DET","NOUN","ADJ"]
freq=[]
nb=[]
temp=[]
for i in range(len(li)):
    temp.append(li[i][4])

for i in range(len(uni)):
    freq.append(temp.count(uni[i])/len(li))
    nb.append(temp.count(uni[i]))

unigram=[freq, nb, uni]
print(unigram)


    
    
        
 
