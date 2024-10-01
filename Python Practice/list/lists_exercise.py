# List Exercise 

e = [2200, 2350, 2600, 2130, 2190]

# 1In Feb, how many dollars you spent extra compare to January?

extra_dollars = e[1] - e[0] 
print(extra_dollars)

# 2. Find out your total expense in first quarter (first three months) of the year.
total_exp = 0
for i in range(3):
    total_exp += e[i]
print(total_exp)


# length 
print(len(e))

# append in the list

e.append(2000)

# remove from the list
e.remove(2000)

# insert at specific position
e.insert(e.index(2200),2000)

# replace 
e[0:2] = [1000]

# sort the list 

print(e.sort())

# 3. Find out if you spent exactly 2000 dollars in any month: Pass
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list : Pass
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this : Pass