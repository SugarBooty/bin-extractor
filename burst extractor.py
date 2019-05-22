burst = open("AVIN0001 edit.BNP", "rb")
shot_list = open("shot_list2.txt", "w", newline='\n')
str_len = 12 # length of the string being searched for
str_txt = "DSC" # the text searched for
blank_lines = 0
n = 0

"""
for line in burst:
    str_line = str(line)
    if (str_line.find("DSC") != -1):
        print(str(line))
        print(n)
        print("New Line \n")
        n = n + 1




"""
for line in burst: # goes through every line
    str_line = str(line)
    pos = str_line.find(str_txt)
    pic = str_line[pos-50:pos+50]
    if pos != -1: # if the string was found
        if blank_lines: # if there was blank lines
            #shot_list.write(str(blank_lines) + '\n')
            blank_lines = 0
        shot_list.write(pic + "  |  " + str(pos) + '\n')
    else: # if no string was found
        blank_lines = blank_lines + 1
    print(pic)