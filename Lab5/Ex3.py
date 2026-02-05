survey_responses = [5, 7, 3, 8]
id_values = (1012, 1035, 1021, 1053)

survey_dict = dict(zip(id_values, survey_responses))
print("Survey responses with respondent IDs:", survey_dict)

print(f"Respondent {id_values[2]} gave a response of {survey_dict[id_values[2]]}.")