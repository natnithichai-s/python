#633040585-1
def compute_avg_list():
    num = (input("Enter 5 positive number: "))
    print ("You entered", num)
    nl = num.split()
    print ("Numbers are ", nl)

    for i in range(len(nl)):
        nl[i] = int(nl[i])

    avg = sum(nl) / len(nl)

    print ("The average number of the list is", avg)

def compute_avg():
    list1 = []
    while True:
        num2 = float(input("Enter a positive number: "))
        list1.append(num2)
        if num2 == 0:
            break
    print ("Numbers are ", list1)
    avg2 = sum(list1) / len(list1)
    print ("The average number of the list is",avg2)


if __name__ == '__main__':
    compute_avg_list()
    compute_avg()