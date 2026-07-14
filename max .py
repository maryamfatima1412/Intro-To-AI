# ye function sab se bara number dhoondta hai
def find_max(*numbers):
    return max(numbers)
# numbers ko function mein bheja ja raha hai
result = find_max(1, 5, 3, 9, 2)
print ("The maximum number is:", result)