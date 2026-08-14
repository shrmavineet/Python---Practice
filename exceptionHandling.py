value = int(input("Enter a number that want to divide by 200: "))
try:
    output = 200/value
except Exception as err:
    print("Sorry! There is an error:", err)
else:
    print("Good there is no Exception Error")
finally:
    print("I will run no matter what")

print(output)


######################################################################################################

#raise

age = int(input("Enter your age: "))
try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("Welcome to the club")
except Exception as err:
    print(f"An error occured as: {err}")


print("Club avaliable soon")