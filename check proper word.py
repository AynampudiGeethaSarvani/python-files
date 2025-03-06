def check_upper_case(word):
    f=False
    if word.isupper() or word.islower():
        f=True
    if word[0].isupper() and word[1:].islower():
        f=True
    return f
s=input('enter')
print(check_upper_case(s))
