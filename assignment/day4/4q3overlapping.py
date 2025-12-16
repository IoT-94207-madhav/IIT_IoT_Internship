l1=[1,2,3,4,5,6,7,8,9]

l2=[0,0,0,0,0,0,0,0,0]

def overlapping(l1, l2):
    return bool (set(l1) & set(l2))

a=overlapping(l1,l2)
print("result",a)