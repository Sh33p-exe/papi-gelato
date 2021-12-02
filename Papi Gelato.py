vraag1 = "True" 
vraag2 = "True"
vraag3 = "True"
print ("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
#Stap 1
while vraag1 == "True":
    bolletjes = int(input("Hoeveel bolletjes wilt u? "))

    if bolletjes <= 8 and bolletjes >= 4:
        vraag1 = "False"
        print ("Dan krijgt u van mij een bakje met",bolletjes,"bolletjes")
        hob = 'bakje'

    elif bolletjes <= 3:
        vraag1 = "False"
        #Stap 2
        while vraag2 == "True":
            boh = input("Wilt u deze "+ str(bolletjes) +  " bolletje(s) in een hoorntje of een bakje? ")
            if boh == ("hoorntje" or "bakje"):
                vraag2 = "False"
                if boh == "hoorntje":
                    hob = 'hoorntje'
                elif boh == "bakje":
                    hob = 'bakje'
            else:
                print ("Sorry, dat snap ik niet...")
    elif bolletjes > 8:
        print ("Sorry, zulke grote bakken hebben we niet")

    else:
        print ("Sorry, dat snap ik niet...")
            #Stap 3
    while vraag3 == "True":
        meerBestellen = input("Hier is uw " + hob + " met "+ str(bolletjes) +" bolletjes. Wilt u nog meer bestellen? (ja/nee) ")
        if meerBestellen == "ja":
            vraag1 = "True"
            vraag3 = "False"

        elif meerBestellen == "nee":
            print ("Bedankt en tot ziens!")
            vraag3 = "False"

        else:
            print ("Sorry dat snap ik niet")