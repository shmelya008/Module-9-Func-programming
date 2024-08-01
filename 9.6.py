def all_variants(text):
    for elem in range(len(text)):
        yield text[elem]
    for elem in range(len(text[:1])):
        yield text[elem:2]
    for elem in range(len(text[1:2])):
        yield text[1:3]
        yield text[0:3]


a = all_variants("abc")
for i in a:
    print(i)
  
