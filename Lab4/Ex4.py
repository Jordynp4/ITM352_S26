# try ot append to a tuple. it wont work!

survey_responses = (1012, 1035, 1021, 1053)
print("Original survey responses tuple:", survey_responses)

#survey_responses.append(1054)  # This will raise an AttributeError
survey_responses = survey_responses + (1054,)
print("After adding 1054:", survey_responses)