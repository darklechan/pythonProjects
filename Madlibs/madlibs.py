#String concatenation exercise
# phrase = "Berry"

# #print it
# print("hi sis! " + phrase)

# #another way to print it
# print("hi sis! {}".format(phrase))

# #another way to print it but with the F string. Theses is the clear way to do it
# print(f"hi sis! {phrase}")

adj = input("Adjective: ") #get the user input
verb1 = input("Verb: ")
verb2 = input("Verb: ")
person = input("Person: ")

madlib = f"Play WoW is so {adj}! I want to {verb1} it everyday. Remember to {verb2} and be like {person} :)"
    
print(madlib)
