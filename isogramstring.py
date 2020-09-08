def isogram(str):
    val = str.lower()
    letters = []
    
    for letter in val:
        if letter in letters:
            ret = {f"{letter} already in this sentence"}
            return ret
        else:
            letters.append(letter)
    ret = "no plaggiarism in this sentence"
    return ret


func = isogram
string=str(input("enter string only : "))

val = func(string)
print(val)