import random
import linecache


def restart():
    if (input("voulez vous recommancer? o/n: ")) == "o":
        game()
    else:
        quit()

def game():
    
    n = 0
    i= 10
    word = linecache.getline('French_WordBook.txt', random.randint(1, 22735)).strip()
    f = ""
    test = ""
    user_input = input("lettres?")
    for x in range(len(word)):
        if user_input == word[x]:
            test += user_input
            n+=1
        else:
            test += "_"
            
    if n<1:
        print("il vous reste plus que",i, "erreurs possibles") 
        i -= 1
        
    print(test)
    caracteres = list(test)

    while i>0:
        n=0
        if i == 0:
            print("vous avez perdu, le mot etait: ", word)
        user_input = input("lettres? ")
        for x in range(len(word)):
            if user_input == word[x]:   
                caracteres[x] = user_input
                test = "".join(caracteres)
                n+=1
        if n<1:
            print("il vous reste plus que",i, "erreurs possibles") 
            i -= 1
        print(test) 
        if word == test:
            print("vous avez gagné")
            restart()

    print("vous avez perdue le mot etait: ", word)
    restart()
    
game()


        


  
