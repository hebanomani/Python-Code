x=input("Enter a sentence");
words=x.split();
D={}
for unique in words:
    D.setdefault(unique,words.count(unique));

print(D);
