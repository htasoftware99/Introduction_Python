def make_story():
    f = open("story.txt", "w")
    f.write("Marry had little lamb\n")
    f.write("And then she had some more\n")

make_story()
print(open("story.txt").read())