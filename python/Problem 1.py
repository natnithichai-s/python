#Natnithichai Srikolchan 633040585-1
def compute_avg_list():
    num = (input("Enter 5 positive number: "))
    print ("You entered", num)
    nl = num.split()
    print("Numbers are ", nl)

    for i in range(len(nl)):
        nl[i] = int(nl[i])

    avg = sum(nl) / len(nl)

    print("The average number of the list is", avg)
