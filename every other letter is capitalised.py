def foo(s):
    ret = ""
    i = False  # capitalize
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret
s = input("what text do you want screwed up? ")
text = foo(s)
print(text)
input()
