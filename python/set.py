s=set()
print(type(s))

s={1,"Ajay",76}
print("before updation:",s)

s.update([1,"Ajay",76,"A"])
print("adding grade:",s)

s.remove(76)
print("after removing:",s)

s1=set([1,"Karan",79])
s2=set([2,"Nayan",79])
print("union:",s1|s2)
print("intersection:",s1&s2)
print("difference:",s1-s2)
print("symmetric difference:",s1.symmetric_difference(s2))
