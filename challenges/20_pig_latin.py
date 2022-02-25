def pig_it(text):
    firstLetter = ""
    t_list = text.split()
    for word in t_list:
        firstLetter += word[1:] + word[0] + 'ay' + " "

    if "?" in firstLetter or "!" in firstLetter:
        return firstLetter[:-3]
    else:
        return firstLetter[:-1]
    
    # lst = text.split()
    # return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))
print(pig_it("Quis custodiet ipsos custodes ?"))
