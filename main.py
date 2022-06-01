print("Welcome to the Noodle Shop!")
type = input("What type of noodle would you like? chicken, onion or crayfish? ").lower()
size = input("What plate sizing is required? small, medium or large? ").lower()
prefrence = input("Do you have any prefrences? yes or no? ").lower()

bill = 0

if size == "small":
  bill += 150
elif size == "medium":
  bill += 200
else:
  bill += 250

  

if prefrence == "yes":
  prefrence1 = input("Do you want an egg or a chicken? ").lower() 
  if prefrence1 == "egg":
    bill += 70
    prefrence2 = input("would you like some vegetables? yes or no? ").lower()
    if prefrence2 == "yes":
      bill += 150
    else: 
      bill += 0
  else:
    bill += 100
else:
  bill += 0

extra_pepper = input("Would you like extra pepper? yes or no? ").lower()
if extra_pepper == "yes":
   bill += 10

print(f"Your final bill is ${bill}")