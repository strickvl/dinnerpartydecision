number_of_options= raw_input("Hello, how many options would you like to compare?")
# setting a counter to help iterate through the different options
dish_count = 0
# making a list to store the names of those different options
list_of_options = []
# appends the dish titles to a list ('list_of_options')
while(dish_count<number_of_options):
	list_of_options.append(raw_input("Give a title to option "+str(dish_count+1)+" of " + str(number_of_options)))
	dish_count=dish_count+1
else:
	print("Thank you, " + username + ". Now we will evaluate the weighted criteria.")