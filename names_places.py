# Reading data from files from a user imput
# Created in Sleepy Hollow on November 5, 2015



text_file = open('C:\\Users\\Aneta\\Desktop\\NamesAndPlaces.txt', 'r').read()
text = text_file.split()

#turn the text into a dictionary
names_dic = []
for x in text:
    x = x.split(',')
    names_dic.append(x)

names_dic = dict(names_dic)

print names_dic  #for testing
    
# asking a user to enter a name
name = "not_in_dic"
while name not in names_dic:
    name = raw_input("Enter the name? ")
    if name in names_dic:
        print name, "lives in ", names_dic[name]
    else:
        print "The name was not found... "
    

    

