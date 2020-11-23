
the_word = ('hello my name is #jeff and @i love @you')

text_split = [word for word in the_word.split() if (not word.startswith('@') and  not word.startswith('#'))]
print(text_split)