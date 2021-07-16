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

#Natnithichai Srikolchan 633040585-1
def compute_avg():
    list1 = []
    count = 0
    while True:
        num = int(input("Enter a positive number: "))
        if num < 0 or num == 0:
            break
        else :
            list1.append(num)
            count+=1
    print ("Numbers are ", list1)
    avg = sum(list1) / len(list1)
    print ("The average number of the list is",avg)
compute_avg()
