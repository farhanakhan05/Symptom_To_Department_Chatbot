from Model import predict_department

print("symptoms to department chatbot")
print("type 'exit' to quit")

while True:
    symptoms = input("Enter symptoms: ")

    if symptoms.lower() == "exit":
        print("Goodbye")
        break

    department = predict_department(symptoms)
    print("Recommended Department:", department)
