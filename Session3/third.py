x=input("Enter a sentence");
words=x.split();
D={}
for unique in words:
    D.setdefault(unique,words.count(unique));

print(D);

l=[]

for key in D.keys():
    if D.get(key)>1:
        l.append(key);

l.sort();
print(l);
