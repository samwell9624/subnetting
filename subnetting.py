import random as r

# Dictionary of prefix and subnet
Prefix = {"/30": "255.255.255.252",
          "/29": "255.255.255.248",
          "/28": "255.255.255.240",
          "/27": "255.255.255.224",
          "/26": "255.255.255.192",
          "/25": "255.255.255.128",
          "/24": "255.255.255.0",
          "/16": "255.255.0.0",
          "/8": "255.0.0.0", }

subnet = {"255.255.255.252": "/30",
          "255.255.255.248": "/29",
          "255.255.255.240": "/28",
          "255.255.255.224": "/27",
          "255.255.255.192": "/26",
          "255.255.255.128": "/25",
          "255.255.255.0": "/24",
          "255.255.0.0": "/16",
          "255.0.0.0": "/8"}


# The main function of the programme
def main():
    print("Welcome to the subnetting programme !")
    print("What do you want to do ?")
    print("1. Prefix to subnet")
    print("2. Subnet to prefix")
    print("3. Exit")
    choice = int(input("Your choice : "))
    if choice == 1:
        prefixToSubnet()
    elif choice == 2:
        subnetToPrefix()
    elif choice == 3:
        exit()
    else:
        print("Invalid choice !")
        main()


# Generate the question
def generateQuestion():
    questionPrefix = r.choice(list(Prefix.keys()))
    questionSubnet = r.choice(list(subnet.keys()))
    return questionPrefix, questionSubnet


# Convert the prefix to subnet
def prefixToSubnet():
    # Ask the user how many question he wants to do
    p = int(input("How many question you want to do? "))
    if p == 0:
        exit()
    elif p == 1:
        print("The programme will ask you " + str(p) + " question !")
    elif p > 1:
        print("The programme will ask you " + str(p) + " questions !")

    # Generate the question and ask the user to answer
    for i in range(int(p)):
        questionPrefix, questionSubnet = generateQuestion()
        answer = str(input("What is the prefix of the subnet " + questionSubnet + " ? "))
        print("You answer is " + answer)
        if answer == questionPrefix:
            print("Correct !")
        while answer != questionPrefix:
            answer = str(input("What is the prefix of the subnet " + questionSubnet + " ? "))
            print("You answer is " + answer)
            if answer == questionPrefix:
                print("Correct !")
            else:
                print("Incorrect !")
        print("Correct !")

    # Ask the user if he wants to do more question
    more = input("Do you wants to do more question ? (y/n)")
    if more == "y":
        main()
    else:
        print("Thank you ! Have a nice day !")
        exit()


# Convert the subnet to prefix
def subnetToPrefix():
    # Ask the user how many question he want to do
    p = int(input("How many question you want to do? "))
    if p == 0:
        exit()
    elif p == 1:
        print("The programme will ask you " + str(p) + " question !")
    elif p > 1:
        print("The programme will ask you " + str(p) + " questions !")

    # Generate the question and ask the user to answer
    for i in range(int(p)):
        questionPrefix, questionSubnet = generateQuestion()
        life = 3
        print("You have 3 life to answer this question !")
        answer = str(input("What is the subnet of the prefix " + questionPrefix + " ? "))
        print("You answer is " + answer)
        if answer == questionSubnet:
            print("Correct ! The answer is " + questionSubnet)
        while answer != questionSubnet:
            answer = str(input("What is the subnet of the prefix " + questionPrefix + " ? "))
            life -= 1
            print(f"You have {life} life left to answer this question !")
            if answer == questionSubnet:
                print("Correct !")
            else:
                print("Incorrect !")
            if answer == "Give up":
                life = 0
            if life == 0:
                print("You are out of life!")
                print("The correct answer is " + questionSubnet)
        print("Correct !")

    # Ask the user if he wants to do more question
    more = input("Do you wants to do more question ? (y/n)")
    if more == "y":
        main()
    else:
        print("Thank you ! Have a nice day !")
        exit()


if __name__ == "__main__":
    main()
