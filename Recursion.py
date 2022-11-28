#RECURSION
# 5 simple steps
# 1. What's the simplest possible input?
# 2. Play around with examples and visualize!
# 3. Relate hard cases to simpler cases
# 4. Generalize pattern
# 5. Write code by combining recursive pattern with the base case

# First example
# Write a recursive function that given an input n
# sums all nonnegative integers up to n.
# 1. What's the simples possible input?
#           sum(0) -> 0 (base case)
# 2. Play around with exmamples and visualize!
# 3. Relate hard cases to simpler case
#      can you relate sum(5) and sum(4)?
# 4. Generalize the pattern
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

# Recursive Leap of Faith
# Assume simpler cases work out
# sum(5) = 5 + sum(4)

#Example 2
# Write a function that takes two inputs n and m 
# and outputs the number of unique paths from the top
# left corner to bottom right corner of a n x m grid.
# Constraints: you can only move down or right 1 unit at a time.

# 1. Simplest Possible input
# grid(1,1) = 1 move 
# grid(n,m) -> 1 if n = 1 or m = 1
# 2. Visualize
# 3. Relate to hard case
# 4. generalize the pattern
# grid(n,m) = grid(n,m-1) + grid(n-1,m)
def grid_paths(n ,m):
    if n == 1 or m == 1:
        return 1
    else:
        return grid_paths(n, m-1) + grid_paths(n-1, m)

#Examples 3 (hard question)
# Write a function that counts the number of ways
# you can partition n objects using parts up to m
# (assuming m >= 0)

# 1. Simplest input 
# count_partitions(0,0) -> 1
# count_partitions(0,1) -> 1
# count_partitions(0,2) -> 1
# Base case - count_partitions(n,m) -> 1 if n == 0
# count_partitions(1,0) -> 0
# count_partitions(2,0) -> 0
# Base case 2 - count_partitions(n,m) -> 0 if m == 0
# 2. Visualize (write out many countable case)
# All count_partitions(n,m-1) partitions are also in 
# count_partitions(n,m) ? (yes, after visualize the case)
# count_partitions(n,m-1) is the subset of ..(n,m)
# Used m in partitions
# Generalize: ..(n,m) = ..(n-m,m) + ..(n,m-1)
# 1 if n = 0,  0 if m = 0 or n < 0

def count_partitions(n,m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)



print(count_partitions(3, 2))


#Count number of elements that greater than v in l
def Count(l, x, v, c):
    if x == len(l):
        return c
    elif l[x] > v:
        c += 1
    return Count(l, x+1, v, c)