print("WELCOME TO THE EPIC TAXI GAME")
print("please input a username")
driver = input()
oil = 1000
price = 10
location = 500
import random
print("hello "+driver+", in this game your goal is to earn $10,000 as a taxi driver.");
money = 0
while True:
    print("money: $"+str(money))
    print("gas: "+str(oil)+"/1000")
    print("ride price: $"+str(price))
    print("location: "+str(location))
    print("what would you like to do?")
    print("g = gas refill ($3 (refill anywhere anytime as long as you have money))")
    print("p = give a ride to closest person who wants it")
    print("everyone only wants to go exactly 100 units")
    print("tg5 = tow to g5 (gas station at 500) $10 (in case you get stuck on the road without much gas)")
    print("qp = increse the quality and price by 5$ (10$) (quality plus)")
    action = input()
    if(action == "p"):
        dist=random.randint(-200, 200)
        print("the closest person was "+str(abs(dist))+" units away, at "+str(location+dist))
        if(oil>dist+100):
            print("also, you got $"+str(price)+":)")
            location+=dist
            money+=price
            oil-=100
            oil-=abs(dist)
        else:
            print("but, unfortunatly you don't have enough gas to get to him and drive to his destination :(")
    if(action == "g"):
        if(money>1):
            oil=1000
            money-=1
            print("GAS METER FULL")
        else:
            print("sorry, you can't afford the gas.")
    if(action == "qp"):
        if(money>=10):
            price+=5
            money-=10
        else:
            print("you need $10 to increse your taxi ride quality/price")
    if(money>=10000):
        break
print("YOU WIN!!")
