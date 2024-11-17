def largest(sticks):
    sticks.sort()
    for i in range(len(sticks)-1,1,-1):
        if sticks[i-2]+sticks[i-1]>sticks[i]:
            return sticks[i-2]+sticks[i-1]+sticks[i]
    return -1
n=int(input())
sticks=list(map(int,input().split()))
result=largest(sticks)
print(result)
