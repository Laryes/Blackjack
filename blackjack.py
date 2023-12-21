import random

giris = input("giriş yapıcak mısınız Y/N")


if  giris == "Y" :
        print("oyuna girildi")
        bet = int(input("bet miktarını girin"))
        x = random.randint(1,10)
        y = random.randint(1,10)
        y1 = random.randint(1, 10)
        o = x
        k = y + y1

        if y == 1:
            y = 11
            k = y + y1

        elif y1 == 1:
            y1 = 11
            k = y + y1
        elif y1 == 11 & y == 11:
            y = 11
            y1 = 1
            k = y1 + y

        if x == 1:
            x = 11
            o = x
            print("x 1 di")
            print("kartınız = ", o)
            giris = input("Kart çekiyor musunuz Y/N")
        if giris == "Y":
            x1 = random.randint(1,10)
            o += x1
            print("Kartınız",o)

            for i in range(5):
                s = input("Kart çekiyor musunuz Y/N")
                if s == "Y":
                    x1 = random.randint(1, 10)
                    o += x1
                    print("kartınız", o)
                else:
                    print("kartınız", o)
                    break
                if o > 21:
                    print("kaybettiniz")
                    break



            for i in range(5):
                print("kurpiyer sayı çeker", k)
                if o > 21 :

                    break
                elif k < o :
                    if k < 17:
                        y2 = random.randint(1, 10)
                        k += y2
                    elif k > o:
                        print("kaybettniz")
                    elif k < o :
                        bk = bet * 2
                        print("kurpiyer kaybeder", "kazançK", bk)
                        break


                else:
                    break
            if o > 21:
                print("kaybettiniz", o)
            elif o <= 21:
                for i in range(1):
                    if o == 21:
                       print("kurpiyer açar" , k)
                       if k < 17:
                           for i in range(4):
                             print("kurpiyer sayı çeker" , k)
                             if k < 17:
                                    y2 = random.randint(1, 10)
                                    k += y2
                             elif k == 21:
                                 print("berabere")
                             else:
                                # print("kurpiyerin sayısı", k ,"kurpiyer kaybeder")
                                 #bk = bet * 2
                                # print("kazanç",bk)
                                 break
                    elif k == o:
                        print("berabere")
                        break
                    elif k > 21 & o > 21:
                        print("berabere")
                        break
                    elif o > 21:
                        break
                    elif o > 21:
                        print("Oyuncu kaybeder")
                        break
                    elif k > 21:
                        bk = bet * 2
                        print("kurpiyer kaybeder" , bk)
                        break
                    elif k > o:
                        print("kaybettiniz")
                        break
                    elif o == 21 & k < 21:
                        bk = bet * 2
                        print("kazandınız",bk)
                        break
                    elif k > 21 & o <= 21:
                        bk = bet * 2
                        print("kurpiyer kaybeder", "kazançK", bk)
                        break
                    elif k > o:
                        print("kurpiyer kazandı","kaybettniz")
                        break






        elif k == 21:
           print("kaybettiniz")


        #if k > o:












else:
    print("oyuna girilmedi")

