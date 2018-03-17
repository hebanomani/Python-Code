def fact(n):
    if n==1:
        return 1;
    else:
        return n*fact(n-1);

#ans=fact(5);
#print(ans)

    

def factorialList(a,b):
    global l
    l={};
    for each in range(a,b):
        l.setdefault(each,fact(each));

    return l;

ans=factorialList(5,8)
print(ans)
print(ans[6]);
