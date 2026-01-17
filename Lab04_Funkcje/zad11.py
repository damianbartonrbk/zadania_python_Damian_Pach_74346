def odwroc_string(tekst):
    if tekst == "":
        return tekst
    return odwroc_string(tekst[1:]) + tekst[0]
print(odwroc_string("python"))