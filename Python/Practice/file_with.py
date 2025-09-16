with open('example.txt', 'r+') as file:
    content = file.read()
    #file.write('\nBatch V-17')

print(content)
file.write("bla")

