# CTI-110
#P2HW2-Tip, Tax, and Total
# Larry Richardson
# 18 February 2018

#get the total of food cost
totalfoodcost= float(input('Enter the cost for food:'))

#Get the tip amount(18%)
tip= totalfoodcost*.18

#Get the sales tax(7%)
saletax= totalfoodcost*.07

#Get totalcost
totalcost=(totalfoodcost+tip+saletax)

#display the total cost
print('total cost:',format(totalcost+tip+saletax,',.2f'))

#display the tip amount
print('tip amount:',format(tip,'.2f'))

#Display the sale tax
print('sale tax:',format(saletax,',.2f'))
                         
                           
