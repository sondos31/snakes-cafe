print( "Welcome to the Snakes Cafe")
print("Appetizers\nWings\nCookies\nSpring RollsEntrees\nSalmon\nSteak\nMeat Tornado\nA Literal Garden\nDesserts\nIce Cream\n,Cake\n,Pie\nDrinks\nCoffee\nTea,Unicorn Tears\n")
list1=["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn","Tears"]


def orders():

       count = 0
       order =""
       while order!='quit':
        print("What would you like to order?")
        order = input(">")
        if order =='quit':
            break
        count = count + 1
        print(f'** {count} order of {order} have been added to your meal**')

orders()