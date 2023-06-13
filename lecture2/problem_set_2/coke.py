

def valid_amount(amount, total):
    try: 
        amount = int(amount)
        if amount == 25 or amount == 10 or amount == 5:
            newTotal = total - amount
            return newTotal
        else:
            return total 

    except:
        main()

def flow(n):
     prices = n
     while(True):
        changeAmount = valid_amount(input("Insert Coin: "),prices)
        if changeAmount != prices and not changeAmount == 0 :
            print(f"Amount Due: {changeAmount}")
            prices = changeAmount
        elif changeAmount == 0 :
            print(f"Change Owed: {changeAmount}")
            break
        else:
            continue


def main():
     totalAmount = 50
     print(f"Amount Due: {totalAmount}")
     flow(totalAmount)

if __name__ =="__main__":
    main()
   
