def remove_exclamation_marks(s):
    return s.translate(s.maketrans("Hello World!", "Hello World!", "!"))
print(remove_exclamation_marks("Hello World!!!"))