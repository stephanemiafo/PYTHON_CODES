def copy(fi, gi):
    with open(fi, 'r') as test, open(gi, 'w') as doc:        # COPY THE CONTENT OF fi, AND WRITING TO gi
        # copy
        vi = test.read()                                     # RETURN THE CONTENT OF fi as a string
        # paste
        vi = doc.write(vi)                                   # WRITING THE CONTENT OF fi INTO gi

file1 = 'nile.txt'                                           # existing file to copy
file2 = 'copy_nile.txt'                                     # DOES NOT MATTER WHETHER IT EXIST OR NOT
copy(file1, file2)