## Covered topics
- context manager
- file handling


### context manager
- context manager are statements which have a start end exit and also code block of the statement is executed withing this context.
Syntax: with open(file_name, mode) as obj_name:
            code block


### File Handling
Syntax - open(file_name, mode) -> return file object
mode -> r, w, a, x(create and write to file)
note: add b for binary

For writing to a file: file_obj.write(content)
For reading in text mode: file_obj.read() # To read whole file
                          file_obj.readline() # To read a line
                          file_obj.readlines() # To read all the lines


### Assignment
- Create and write something in a file and then read the file and print the content, using with statement.