import os


print("Hello New Student! What would you like to know about?\n")

answer = ""
while answer != "exit":
      answer = input("Here are some suggested Questions:\n"
            "1. Tell me more about Amador\n"
            "2. Map of Amador (Where are the classrooms and bathrooms)\n"
            "3. Student Resources\n"
                     "'exit' to exit\n"
            "Or feel free to write whatever: ")

      if 'bathroom' in answer:
            print ("The bathroom is in the builing")
      else:
            print ("I'm sorry, I don't understand. Please check your spelling and retry")

