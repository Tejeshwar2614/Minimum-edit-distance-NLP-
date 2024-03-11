

# Here this is the code for finding the minimum edit distance of one word to n other words 
# Whereas the n other words will be read through file 
# Here the algorigthm will read each word from the file and find the minimum edit distance between the given word and the word which we have read from the file

# function is for calculated the minimum edit distance between two words 

def minDistance(string1,string2):
    matrix = []
    a = []
    a.append('r')
    a.append('#')
    for i in string1:
        a.append(i)
    matrix.append(a)
    a = []
    a.append('#')
    for i in range(len(string1)+1):
        a.append(i)
    matrix.append(a)
    for i in range(len(string2)):
        t = []
        for j in range(len(string1)+1):
            if j==0:
                t.append(string2[i])
            if j==0:
                t.append(i+1)
            else:
                t.append(1)
        matrix.append(t)
    for i in range(2,len(matrix)):
        for j in range(2,len(matrix[0])):
            if matrix[0][j]==matrix[i][0]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                t = min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])
                matrix[i][j] = t+1
    return matrix[len(matrix)-1][len(matrix[0])-1]


# Here i am reading the file

word1 = input("enter the word : ")
file  = open('C:\\Software\\Programming_WorkSpace\\pythoncode\\DSA_in_JAVA\\DSA_in_python\\python project\\file.txt','r')
c=1
m = 10
b_w = ''
for line in file:
    words = line.split()
    for i in words:
        word2 = i
        print(str(c)+". ","the minimum edit distance between",word1,"and",word2,"is : ",minDistance(word1,word2))
        if m>minDistance(word1,word2):
            m = minDistance(word1,word2)
            b_w = word2
    c+=1
    print('\t')
print('the word which have the minimum edit distance from the given word is :',b_w,'with the editDistance of:',m)

