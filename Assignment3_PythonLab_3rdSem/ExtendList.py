"""
Extend a given nested list by adding the sub list ["h", "i", "j"] in such a way that it will look like the following expected list.
Given_List: ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Expected_List: ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
"""
given_lst = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
nested_lst = given_lst[2][1][2]
nested_lst.insert(2,'h')
nested_lst.insert(3,'i')
nested_lst.insert(4,'j')
print(given_lst)