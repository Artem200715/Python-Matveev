from string import ascii_lowercase
string_new = "hello, I`m  stUdent in RkSi"


def str1(words):
    endin = ""
    for i in words:
        if i in ascii_lowercase:
            i = i.upper()
            yield endin + i
        else:
            yield endin + i


nig = ""
ending = str1(string_new)
for n in ending:
    nig += n
print(nig)
