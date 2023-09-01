from replit import clear
bid_list = {}
def highest_bid_finder(bidding_record):
    highest=0
    winner = ""
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount>highest:
            highest=bidding_amount
            winner = bidder
    print(f"The winner is {winner} with highest bid of ${highest} ")
cont = True
while cont == True:
    name = input("Enter Your name\n")
    bid = int(input("Enter you Bid\n$"))
    bid_list[name]=bid
    anyone_else = input("is there any other bidder?\nIf yes kindly type yes else no\n").lower()
    
    if anyone_else=='yes':
        cont=True
        clear()
    elif anyone_else=='no':
        cont=False
    else:
        print("kindly answer in the question correctly")
        anyone_else = input("is there any other bidder?\nIf yes kindly type yes else no\n").lower()
        if anyone_else=='yes':
            cont=True
    
        elif anyone_else=='no':
            cont=False
print(highest_bid_finder(bid_list))

    


