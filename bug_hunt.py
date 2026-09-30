count = 1
total = 0

# BUG: Added the missing colon so the while loop has a valid header.
# BUG: Changed < 5 to <= 5 so the loop includes 5 in the sum.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Used an f-string to format total as text instead of concatenating an integer.
print(f"Sum of 1 to 5 is: {total}")
