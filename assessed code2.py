def showmenu():
    print ("________________________________")
    print ("Enter choice:")
    print ("1: Show words")
    print ("2: Show clues")
    print ("3: Guess a pairing")
    print ("9: Exit game")
    
    while ask!="9":
        global ask
        ask = input("Enter choice >>")
        if ask == "9":
            exitgame()
        else:
            if ask == "1":
                showwords()
            elif ask == "2":
                showclues()
            elif ask == "3":
                substitute()
            showmenu()          
   
def exitgame():
    print("goodbye!")
    return

def showwords():
    # show list of word from words.txt
    words = open('words.txt', 'r')
    print(words.read())
    return
def showclues():
    # show list of clues from clues.txt
    clues = open('clues.txt', 'r')
    print(clues.read())
    return

# show list of words with clues substituted
#for line in words:
    #print (line)
def substitute():

    ask2 = input("Enter symbol & letter pair >>")
    if len(ask2)>2:
        print ("________________________________")
        print ("******* invalid input only 2 characters please ********")
        print ("________________________________")
        return
    
    
    global newdata
    newdata = newdata.replace("#","A")
    newdata = newdata.replace("*","M")
    newdata = newdata.replace("%","N")
    newdata = newdata.replace(ask2[:1],ask2[1:])
    print(newdata)
    return
#enter a letter and symbol pairing
#if letter is already matched - enter another
# if symbol already matched then enter another
# delete a symbole letter pairing
# repatea the last three as inifntium
#check if teh answers are solved against solved,txt
#extend program so it calculates frequency

f = open('words.txt', 'r')
newdata = f.read()
f.close()
ask = ""
showmenu()
