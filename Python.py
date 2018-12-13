import pyautogui as pg
import webbrowser as wb
show = pg.prompt ("What is your favorite show? ")

if show == "Ballers":
    wb.open ("https://www.youtube.com/watch?v=3SlHAwNwiHAhttps://www.youtube.com/watch?v=3SlHAwNwiHA")
elif show == "Ozark":
    wb.open ("https://www.youtube.com/watch?v=5hAXVqrljbs")
elif show == "Eastbound and Down":
    print("Kenny Powers is the G.O.A.T pitcher")
elif show == "Billions":
    wb.open ("https://www.google.com/search?q=david+levien&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi8loPCsbPeAhUkWN8KHRB7ANAQ_AUIDygC&biw=695&bih=609#imgrc=jiq7NYQJBn62aM:")
elif show == "Sports Center":
    wb.open ("https://www.youtube.com/watch?v=dgjg5XszAiM")
elif show == "Riverdale":
    wb.opem ("https://www.youtube.com/watch?v=GWe5D5G0PVE")
elif show == "the office":
    wb.open ("https://www.youtube.com/watch?v=M8KmqaJvgpE")
else:
    wb.open ("https://www.youtube.com/watch?v=AfIOBLr1NDU")

food = pg.prompt ("what is your favorite food? ")

if food == "Jumbo Shrimp":
    wb.open ("https://www.youtube.com/watch?v=T8HtmThgQvw")
elif food == "Bacon":
    wb.open ("https://www.youtube.com/watch?v=98i6s0s_RrM")
    
elif food == "Food":
    wb.open ("https://www.youtube.com/watch?v=tQFbCz9NkB0")
elif food == "Little Ceasers":
    wb.open ("https://www.youtube.com/watch?v=oqq7ALCDGFc")
elif food == "Chicken Dumpling":
    wb.open ("https://www.youtube.com/watch?v=1vrEljMfXYo")
elif food == "Lithiuanian meat":
    wb.open ("https://www.youtube.com/watch?v=N2VwIfi6Lo")
else:
        print (" your favorite food is " + food)

Game = pg.prompt ("What is your favorite Game? ")

if Game == "Call Of Duty Black ops 4":
    wb.open ("https://www.youtube.com/watch?v=k85mRPqvMbE&t=28s")
elif Game == "Fortnite":
    wb.open ("https://www.youtube.com/watch?v=2halApdn_UA")
elif Game == "NBA 2k":
    wb.open ("https://www.youtube.com/watch?v=ZR6Z6q8RjBs")
elif Game == "Madden":
    wb.open ("https://www.youtube.com/watch?v=JribVbv6CV4")
elif Game == "NHL":
    wb.open ("https://www.youtube.com/watch?v=OmVBB52AS8I")   
else:
    print (" your favorite game is " + Game)

Football_Team = pg.prompt ("What is your favorite Football_Team ")
if Football_Team == "New York Giants":
    wb.open ("https://www.youtube.com/watch?v=M_ni48EdmCE")
elif Football_Team == "New England Patriots":
    wb.open ("https://www.youtube.com/watch?v=cLmCJKT5ssw")
elif Football_Team == " Green Bay Packers":
    wb.open ("https://www.youtube.com/watch?v=KNHgeykDXFw")
elif Football_Team == "Dallas Cowboys":
    print ("America's Team I see")
elif Football_Team == "Jacksonville":
    wb.open ("https://www.youtube.com/watch?v=XqZsoesa55w")
elif Football_Team == "Houston":
    print ("You think you are Jurgis")
else:
        print (" your favorite Football_Team + Football_Team ")

Hockey_Team = pg.prompt ("What is favorite Hockey_Team ")

if Hockey_Team == "Rangers":
     wb.open ("https://www.youtube.com/watch?v=5HMObvgyZiY")
elif Hockey_Team == "Bruins":
        wb.open ("https://www.youtube.com/watch?v=nD80G4PdpII")
elif Hockey_Team == "Jets":
    print ("Those Baby Blue Jerseys tho")
elif Hockey_Team == "Coyotes":
    wb.open ("https://www.youtube.com/watch?v=HOXPiG1_GOc")
elif Hockey_Team == "Oilers":
    print ("https://www.youtube.com/watch?v=xDKSCrA6uy8")
elif wb.open == "Leafs":
    print ("Leafs are winning the cup")
else:
    print (" your favorite Hockey_Team is + Hockey_Team ")
