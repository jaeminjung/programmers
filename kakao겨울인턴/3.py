def editDistance(source, target):
    # Write your code here

    for i in range(len(source)):
        # print(ord(source[i]))
        # print(ord(target[i]))

        diff = ord(source[i]) - ord(target[i])
        print(diff)

editDistance("abdh", "bcif")