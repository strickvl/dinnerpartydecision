# Tool to decide what to cook when presented with a number of alternatives

def weighted_criteria_evaluation():
	return "completed criteria evaluation"
	
def run_decision_matrix():
	# establishes the user's name along with the number of options we're evaluating
	username = raw_input("What is your name?")
	number_of_options= int(raw_input("Hello " + username +", how many options would you like to compare?"))
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
	#begins weighted_criteria_evaluation
	weighted_criteria_evaluation()


# Give a title/name to option 1 of x
# (repeat as per number of options)

# Thank you, {{name}}, now we are going to evaluate the weighted criteria.

# How important is the cost of ingredients / utensils?

# How important is it that the recipe has minimal preparation stress?

# How important is it that others are able to help cook?

# How important is it that it doesn't need new cooking utensils?

# How important is it that the recipe be lip-smackingly tasty?

# How important is it that the recipe takes only a short time to prepare?

# How important is the excitement/novelty factor of the recipe?

# How important is it that the recipe produces a lot of food (by volume)?

# How important is it that the recipe is a social-food with sharing potential?

# How important is it that the recipe is able to generate discussion among guests?

# How important is it that the number of ingredients required is minimal?

# The following questions apply to option 1 (the ...): (rate on a scale of 1-10)
# How expensive are the ingredients?
# How likely is it that the recipe will be stress-free?
# What is the potential for outside-help supporting the cooking?
# To what extent are new cooking utensils required?
# How lip-smackingly tasty will the recipe likely be?
# How long will the option take to prepare?
# How much novelty-factor does the option bring to the table?
# How much food (by volume) will the option generate?
# Is the option good for sharing and being social around?
# To what extent will the option be able to generate discussion among guests?
# To what extent are ingredients not already in the house required?

# (repeat for all options)

# [CALCULATE THE SCORES]

# I have considered the options, and can give you the final scores as follows:

# TOP PICK: Option X, the ..., with score xxx.xxx
# RUNNER'S UP: the xxx with score xxx.xx
# 			the xxx with score xxx.xx

# For this reason, I'd recommend you cook the xxx for your dinner party.

run_decision_matrix()