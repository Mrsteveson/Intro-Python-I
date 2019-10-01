"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
# Open the file, including the correct file path, utilize .read, "r" = read.
with open("src/foo.text", 'r') as file:
    txt = file.read()
print(txt)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
stuff = ["Learning python.", "It is kinda neat.", "Code challenges still kick me in the teeth."]

with open("src/bar.text", "w") as f:    # "w" = write
    for x in stuff:
        f.write(x)  # Write each line
        f.write("\n") # Create a new line

