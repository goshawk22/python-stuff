input1 = input("Enter a string: ")
input2 = int(input("Enter num letters to remove: "))

input1 = input1[:-input2]

m = input("Do you want an m with that? > ")
if (m == 'yes') or (m == 'Yes'):
    input3 = "m"
    input4 = input1 + input3
    print(input4)

else:
    print(input1)