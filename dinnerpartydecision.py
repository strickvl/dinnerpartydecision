import operator
# Tool to decide what to cook when presented with a number of alternatives
	
def run_decision_matrix():
	# establishes the user's name along with the number of options we're evaluating
	username = raw_input("What is your name?")
	number_of_options = int(
		raw_input(
			f"Hello {username}, how many options would you like to compare?"
		)
	)
	# setting a counter to help iterate through the different options
	dish_count = 0
	# making a list to store the names of those different options
	list_of_options = []
	# appends the dish titles to a list ('list_of_options')
	while (dish_count<number_of_options):
		list_of_options.append(
			raw_input(
				f"Give a title to option {str(dish_count + 1)} of {number_of_options}"
			)
		)
		dish_count += 1
	else:
		print(
			f"Thank you, {username}. Now we will evaluate the weighted criteria. Please use numbers from 1-10."
		)
	# begins weighted_criteria_evaluation
	# gathers data on the various factors that will contribute
	crit_cost=int(raw_input("How important is the cost of ingredients / utensils?"))
	crit_stress=10-int(raw_input("How important is it that the recipe has minimal preparation stress?"))
	crit_support=int(raw_input("How important is it that others are able to help cook?"))
	crit_utensils=int(raw_input("How important is it that it doesn't need new cooking utensils?"))
	crit_taste=int(raw_input("How important is it that the recipe be lip-smackingly tasty?"))
	crit_time=10-int(raw_input("How important is it that the recipe takes only a short time to prepare?"))
	crit_novelty=int(raw_input("How important is the excitement/novelty factor of the recipe?"))
	crit_volume=int(raw_input("How important is it that the recipe produces a lot of food (by volume)?"))
	crit_social=int(raw_input("How important is it that the recipe is a social-food with sharing potential?"))
	crit_discussion=int(raw_input("How important is it that the recipe is able to generate discussion among guests?"))
	crit_ingredients=int(raw_input("How important is it that the number of ingredients required is minimal?"))
	crit_eco_distance=int(raw_input("How important is it that the meal be eco-friendly in terms of distance of ingredient travel?"))
	crit_eco_ethics=int(raw_input("How important is it that the meal be ethically sound in terms of the ingredients?"))

	# begins evaluation of each cooking option, gathering the scores
	options_evaluation=[]
	for options_counter in range(number_of_options):
		options_evaluation.append({})
		print(
			f"The following questions apply to {list_of_options[options_counter]}. Please rate on a scale of 1-10."
		)
		cost=int(raw_input("How expensive are the ingredients?"))
		options_evaluation[options_counter]['cost']=cost
		stress=int(raw_input("How stressful will this meal/option likely be to prepare?"))
		options_evaluation[options_counter]['stress']=stress
		support=int(raw_input("What is the potential for outside-help supporting the cooking?"))
		options_evaluation[options_counter]['support']=support
		utensils=int(raw_input("To what extent are new cooking utensils required?"))
		options_evaluation[options_counter]['utensils']=utensils
		taste=int(raw_input("How lip-smackingly tasty will the recipe likely be?"))
		options_evaluation[options_counter]['taste']=taste
		time=int(raw_input("How long will the option take to prepare?"))
		options_evaluation[options_counter]['time']=time
		novelty=int(raw_input("How much novelty-factor does the option bring to the table?"))
		options_evaluation[options_counter]['novelty']=novelty
		volume=int(raw_input("How much food (by volume) will the option generate?"))
		options_evaluation[options_counter]['volume']=volume
		social=int(raw_input("Is the option good for sharing and being social around?"))
		options_evaluation[options_counter]['social']=social
		discussion=int(raw_input("To what extent will the option be able to generate discussion among guests?"))
		options_evaluation[options_counter]['discussion']=discussion
		ingredients=int(raw_input("To what extent are ingredients not already in the house required?"))
		options_evaluation[options_counter]['ingredients']=ingredients
		eco_distance=int(raw_input("Have ingredients had to be imported / travel from a long distance?"))
		options_evaluation[options_counter]['eco_distance']=eco_distance
		eco_ethics=int(raw_input("How ethically sound is this option in terms of the choice of ingredients (meat etc)?"))
		options_evaluation[options_counter]['eco_ethics']=eco_ethics
	# Score calculation process

	final_score=[]
	for i in options_evaluation:
		cost_final=crit_cost*i['cost']
		stress_final=crit_stress*i['stress']
		support_final=crit_support*i['support']
		utensils_final=crit_utensils*i['utensils']
		taste_final=crit_taste*i['taste']
		time_final=crit_time*i['time']
		novelty_final=crit_novelty*i['novelty']
		volume_final=crit_volume*i['volume']
		social_final=crit_social*i['social']
		discussion_final=crit_discussion*i['discussion']
		ingredients_final=crit_ingredients*i['ingredients']
		eco_distance_final=crit_eco_distance*i['eco_distance']
		eco_ethics_final=crit_eco_ethics*i['eco_ethics']
		total_score=cost_final+stress_final+support_final+utensils_final+taste_final+time_final+novelty_final+volume_final+social_final+discussion_final+ingredients_final+eco_distance_final+eco_ethics_final
		final_score.append(total_score)

	final_dict = {
		list_of_options[dict_counter]: final_score[dict_counter]
		for dict_counter in range(number_of_options)
	}
	# Print final results

	print("I have considered the options, and can give you the final scores as follows:")
	print(final_dict)

# TOP PICK: Option X, the ..., with score xxx.xxx
# RUNNER'S UP: the xxx with score xxx.xx
# 			the xxx with score xxx.xx

# For this reason, I'd recommend you cook the xxx for your dinner party.

run_decision_matrix()