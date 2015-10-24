from sys import argv # import module argv

script, file_name = argv # assign or unpack argv into variables

txt = open(file_name) # open the file and assign contents to variable

print "Here's your file %r:" % file_name # display raw file name
print txt.read()# display raw contents of file

txt.close()

"""
print "Type the filename again:" # prompt user to enter file name again
file_again = raw_input("> ") # change cursor and wait for user to enter

txt_again = open(file_again)# open the file and assign contents to variable again

print txt_again.read()# display raw contents of file again
"""
