                        #######Assignment 3(INPUT)#######

#####1

txt_inp = input("Enter text here:-\n")

if (" " not in txt_inp):
    char_counter = {}
    #counting no. of occurences of each word/character
    for i in txt_inp:
        char_counter[i] = txt_inp.count(i)
    print(char_counter)
else:
    print("The input should not have spaces.")


######2


    dt = int(input("Day-"))
    mnth = int(input("Month-"))
    yr = int(input("Year-"))

    if (yr % 4 == 0):
        if (yr % 400 == 0):
            leap_yr = True
        elif (yr % 100 != 0):
            leap_yr = True
    else:
        leap_yr = False


    def last_date(month):
        if (month % 2 == 1):
            if (month <= 7):
                lst_dt = 31
            if (month > 7):
                lst_dt = 30
        if (month % 2 == 0 and month != 2):
            if (month <= 7):
                lst_dt = 30
            if (month > 7):
                lst_dt = 31
        if (month == 2):
            if leap_yr == True:
                lst_dt = 29
            if leap_yr == False:
                lst_dt = 28
                if dt == 29:
                    print("Invalid Input. Please try again!")
        return lst_dt


    if (1 <= mnth and mnth <= 12 and 1 <= dt and dt <= 31 and 1800 <= yr and yr <= 2025):
        if (dt <= last_date(mnth)):
            if (dt == last_date(mnth) and mnth != 12):
                dt = 1
                mnth = mnth + 1
            elif (dt == 31 and mnth == 12):
                dt = 1
                mnth = 1
                yr = yr + 1
            else:
                dt = dt + 1
            print(f"Next date is: {dt}/{mnth}/{yr}")
    else:
        print("Error!! Year not in Range.")

  ####3

my_list = [3, 9, 10]
sq_list = []
for i in my_list:
    sq_tup = (i, i ** 2)
    sq_list.append(sq_tup)
print(sq_list)

####4

grd_pt = int(input("Grade:- "))
print("For Grade", grd_pt, "Output is:")
if (grd_pt>=4 and grd_pt<=10):
    if (grd_pt == 4):
        ltr_grd = "D"
        perf = "poor"
    elif (grd_pt == 5):
        ltr_grd = "C"
        perf = "below average"
    elif (grd_pt == 6):
        ltr_grd = "C+"
        perf = "average"
    elif (grd_pt == 7):
        ltr_grd = "B"
        perf = "good"
    elif (grd_pt == 8):
        ltr_grd = "B+"
        perf = "very good"
    elif (grd_pt == 9):
        ltr_grd = "A"
        perf = "excellent"
    elif (grd_pt == 10):
        ltr_grd = "A+"
        perf = "outstanding"
    print(f"Your Grade is '{ltr_grd}' and {perf} performance.")

else:
    print("Error!!")



###5

n = int(input("Number:"))

a2z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n):
    if 2*i<n:
        j = a2z[:n-2*i]

        print(" "*i, j)


####6

dict1 = {}
while True:
    name = input("Enter your name: ")
    SID = int(input("Enter your SID %s: " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    while True:
        more_data = input("Do you want to enter more data? \n")
        if more_data in ("N", "n", "No", "no", "NO"):
            more_data = 0
            break
        elif more_data in ("Y", "y", "Yes", "yes", "YES"):
            more_data = 1
            break
        else:
            print("Please say yes or no")
            continue
    if more_data == 0:
        break

#(a)
print("\n(a). Students Details:")
for i in dict1:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict1[i],i))

#(b)
dict2 = {}
for sorted_value in sorted(dict1.values()):
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\n(b). Students Details (sorted with respect to names):")
for i in dict2:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict2[i],i))

#(c)
dict3 = {}
for sorted_key in sorted(dict1):
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\n(c). Students Details (sorted with respect to SIDs):")
for i in dict3:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict3[i],i))

#(d)
print("\n(d). ", end=" ")
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print("The name of student whose SID is %d is \033[1m%s\033[0m" % (search_SID,dict1[search_SID]))
        break
    else:
        print("The SID you entered isn't entered. \nPlease enter a valid SID to be searched. \nList of valid SIDs: %s\n" % list((dict1.keys())))
        continue





###7

def fibo(n):
    if n==1 or n==2:
        return 1

    return fibo(n-1)+fibo(n-2)

n = int(input("Enter n:\n"))

j = 0
for i in range(1, n+1):
    print(f"{fibo(i)}", end = ",")
    j = j+fibo(i)
print(end = "\n")

# Average of resultant Fibonacci Series.
print(j/n)



###8


#Given Sets
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

#(a).
set_a = (set1 | set2) - (set1 & set2)
print("Part (a):", set_a)

#(b).
set_b = (set1 | set2 | set3) - (set1 & set2) - (set2 & set3) - (set3 & set1)
print("Part (b):", set_b)

#(c).
set_c  =(set1 & set2) | (set2 & set3) | (set3 & set1) | (set1 & set2 & set3)
print("Part (c) :", set_c)

set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#(d).
set_d = set4 - set1
print("part (d):", set_d)

#(e).
set_e = set4 - (set1 | set2 | set3)
set_E = sorted(set_e)
print("part (e):", set_E)





