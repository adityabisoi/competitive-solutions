arr = [5, 5, 10, 100, 10, 5]
rob1,rob2=0,0
for i in arr:
    temp=max(i+rob1,rob2)
    rob1=rob2
    rob2=temp
print(rob2)
