while true:
  user_input=input ("Enter Symptoms(on type exit)")
  if user_input.lower()="exit":
  break
  print("Suggested Department:",predict department(user input))
