# define a list of survey respones values
# define a tuple of ID values 
# append the tuple to the list. Print the list.

#survey_responses = [5, 7, 3, 8]
#id_values = (1012, 1035, 1021, 1053)
#survey_responses.append(id_values)
#print("Survey responses with IDs:", survey_responses)

survey_responses = [(1012, 5), (1035, 7), (1021, 3), (1053, 8)]
survey_responses.sort()
print("Sorted survey responses with IDs:", survey_responses)