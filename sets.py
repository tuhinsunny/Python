s={1,2,'Sparta',2}#duplicates not printed in output
print(s)
print(type(s))
s.add("Hello World")
print(s)
s.update(["abc","xyz"])
print(s)
s.remove(1)
print(s)
s2={5,6,'ABC',98,2}
print(s.union(s2))
print(s.intersection(s2))