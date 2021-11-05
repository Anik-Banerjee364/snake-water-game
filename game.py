import random
print("WELCOME TO SNAKE WATER GAME \n")
print("enter w for water s for snake and g for gun \n")
lst= ["s" , "w" , "g"]
chances=10
c=1
machine_score=0
human_score=0 
while(c<11):
    c=c+1
    input_user=input("Snake water gun :")
    machine_entry=random.choice(lst)
    if(machine_entry == input_user):
        print("Attempt tied\n")
        print(f"your entry {input_user} and computer entry is{machine_entry} \n")
        print("both will get 1 point each \n")
    

        machine_score = machine_score +1
        human_score = human_score+1
        print(f"Your score is {human_score} and computer scoren is {machine_score}\n")
    elif input_user == "s" and machine_entry=="w":
        print("congo you won this attempt\n")
        print(f"your entry {input_user} and computer entry {machine_entry} \n")
        human_score=human_score+1
        print(f"Your score is {human_score} and computer score is {machine_score}\n")
    elif input_user == "w" and machine_entry == "g":
        print("congo you won this attempt")
        print(f"your entry {input_user} and computer entry {machine_entry} \n")
        human_score = human_score +1
        print(f"Your score is {human_score} and computer score is {machine_score}\n")
    elif input_user == "g" and machine_entry=="s":
        print("congo you won this attempt")
        print(f"your entry {input_user} and computer entry {machine_entry} \n")
        human_score = human_score+1
        print(f"Your score is {human_score} and computer score is {machine_score}\n")
    else:
        print("sorry you lost attempt")
        machine_score = machine_score +1
        print(f"your entry {input_user} and computer entry {machine_entry} \n")
        print(f"Your score is {human_score} and computer score is {machine_score}\n")

if(machine_score > human_score):
    print("machine wins\n")
    print(f"Your score is {human_score} and computer score is {machine_score}\n")
else:
    print("you win\n")
    print(f"Your score is {human_score} and computer score is {machine_score}\n")



