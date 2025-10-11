with open('test.txt','r') as reader:
    content = reader.readlines()
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)


