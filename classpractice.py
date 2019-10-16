# Troy Jeffrey
#10.14.19
# In-class practice

cookies = []
candy = []

def cookie_input():
    for i in range(0,6):
        cookies.append(int(input(">")))

def candy_input():
    for i in range (0,6):
        candy.append(int(input(">")))

def average_cookiesales1():
    return print(f"\nYour average monthly  sales for cookies is: {round(total1/6, 2)}")

def average_candysales():
    return print(f"\nYour average monthly  sales for candy is {total2/6}")

def maximum_cookies():
    return print(f"The maximum for cookies is:{max(cookies)}")

def maximum_candy():
    return print(f"The maximum for cookies is:{max(candy)}")

def minimum_cookies():
    return print(f"The minimum for cookies is:{min(cookies)}")

def minimum_candy():
    return print(f"The minimum for candy is:{min(candy)}")


print("Enter sales for cookies from the last 6 months")
cookie_input()
total1 = int(sum(cookies))
average_cookiesales1()
maximum_cookies()
minimum_cookies()

print("Enter your sales for candy for the last 6 months")
candy_input()
total2= int(sum(candy))
average_candysales()
maximum_candy()
minimum_candy()

if sum(candy) > sum(cookies):
    print("Candy is more popular at the bakery")
else:
    print("cookies is more popular at the bakery")


