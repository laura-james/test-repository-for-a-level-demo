#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Laura
#
# Created:     17/09/2016
# Copyright:   (c) Laura 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
mylist = []
itemadd = ""
def additem():
    while True:
        itemadd = raw_input('Enter item to add to list or q to finish')
        if itemadd != "":
            return itemadd
        if itemadd == "":
            print('Please enter item')

def checklistforduplicate(itemadd):
        if itemadd in mylist:
            print('Item already exists in list')
        else:
            mylist.append(itemadd)

while itemadd != "q":
    print('Lists')
    itemadd = additem()
    if itemadd == "q":
        break
    checklistforduplicate(itemadd)
    print(mylist)

print("Finished")
print(mylist[0])