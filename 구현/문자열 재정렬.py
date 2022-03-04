input = "K1KA5CB7"
num = 0
char = ""

for target in input:
    try:
        target = int(target)
        num += target
    except:
        char += target

print("".join(sorted(char)) + str(num))