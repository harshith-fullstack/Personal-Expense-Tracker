print("==========================")
print("PERSONAL EXPENSE TRACKER")
print("==========================")


personal_expense =[]

user_continue = "yes"



while user_continue =="yes":
  category =input("Category :")
  data =input("Data : ")
  amount_personal =int(input("Enter the Amount :"))
  expense = {
          
         "category": category,
          "date": data,
           "Amount":amount_personal
          }  
    
      
  personal_expense.append(expense)
    
    
  user_continue = input("Do you want to add another expense? yes/no :")
  
print(personal_expense)  
total =0
  
for expense in personal_expense:
    total = total+expense["Amount"]

    print( "CATEGORY:",expense["category"])
    print("DATE:",expense["date"])
    print("TOTAL AMOUNT:",expense["Amount"])
print("Total Amount:",total)
    