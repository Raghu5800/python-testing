try:
    with open('teqst.txt','r') as reader:
        const=reader.read()
        print(const)

except Exception as e:
    print(e)

finally:
    print('done')
    print("D")