t=int(input())

for i in range(t):
    a,b,c,d=map(int,input().split())
    if (a>b):
        f=a
    else:
        f=b
    if (c>d):
        e=c
    else:
        e=d
    print(f+e)