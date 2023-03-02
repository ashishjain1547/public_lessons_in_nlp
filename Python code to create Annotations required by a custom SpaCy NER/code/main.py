from get_annotations import getAnnotatedStrings

with open('test_input_strings.txt') as f:
    lines = f.readlines()

#print(lines)

annotations = []
for i in lines:
    annotations.append(getAnnotatedStrings(i))

with open('output.txt', mode="a") as f:
    for i in annotations:
        f.write(str(i) + "\n")
    

