#1. Real-World Python Dictionary Applications
#Objective: The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods.

#Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions

#Problem Statement: Given the initial menu:


#print(restaurant_menu)


    
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}}
#- Add a new category called "Beverages" with at least two items.
restaurant_menu["Beverages"]= {"Water": 1.00, "Iced Tea": 1.10}
print(restaurant_menu)

#- Update the price of "Steak" to 17.99.
restaurant_menu["Main Course"]["Steak"] = "17.99"
print (restaurant_menu)

#- Remove "Bruschetta" from "Starters". 
del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)