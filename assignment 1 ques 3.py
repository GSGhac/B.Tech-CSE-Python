#Program to write number of seconds and minutes
#Taking user input for number of seconds
total_seconds=int(input("Please enter number of seconds:"))
#converting seconds to minutes and seconds
minutes=total_seconds//60
seconds=total_seconds%60
#Displaying the output
print(f"Duration of {total_seconds} is {minutes}mins and {seconds}secs")
