# file ko read mode mein khola ja raha hai
file = open("myfile.txt", "r")
# har line ko print kiya ja raha hai
for line in file:
    print(line.strip())
file.close()