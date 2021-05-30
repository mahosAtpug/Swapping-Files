
def swappingFiles():
    
    file1 = input("Please Enter The Name of The File : ")
    file2 = input("Please Enter The Name of The File To Be Swapped : ")
      
    with open (file1  , "r") as a:
        data_a = a.read()
    with open (file2  , "r") as b:
        data_b = b.read()

    with open (file1 , "w") as a:
        a.write(data_b)
    with open (file2 , "w") as b:
        b.write(data_a)

swappingFiles()



#     file = open(fileName , "r")
#     numberOfWords = 0
#     for line in file: 
#         words = line.split()
#         numberOfWords = numberOfWords + len(words)  

#     print("Total Number of Words In Your Selected File Are :" , numberOfWords)

# countWordsFromFile()
