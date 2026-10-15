import Solutions

# Q1
print("\n")
sentence = "python is easy and python is powerful"
print(Solutions.count_of_words(sentence))
print("\n")

sentence2 = "Find the Frequency of Each Word in a Sentence"
print(Solutions.count_of_words(sentence2))
print("\n")
# ----------------------------------------------------------------------------------------------------

# Q2
print("*"* 45 ,"Q2","*"*45)

input = "banana"
print(Solutions.count_of_chars(input))
print("\n")

input2 = "Cucumber"
print(Solutions.count_of_chars(input2))

print("\n")
# ----------------------------------------------------------------------------------------------------

# Q3
print("*"* 45 ,"Q3","*"*45)

input = "swiss"
print(Solutions.appears_once_word(input))
print("\n")

input2 = "Apple"
print(Solutions.appears_once_word(input2))

print("\n")
# ----------------------------------------------------------------------------------------------------

# Q4
print("*"* 45 ,"Q4","*"*45)

s1 = "listen"
s2 = "silent"
print(Solutions.check_anagram(s1, s2))
print("\n")

s3 = "vile"
s4 = "evil"
print(Solutions.check_anagram(s3, s4))
print("\n")
# ----------------------------------------------------------------------------------------------------

# Q5
print("*"* 45 ,"Q5","*"*45)

input = "programming"
print(Solutions.second_occurence(input))
print("\n")

input2 = "Trespassing"
print(Solutions.second_occurence(input2))
print("\n")
# ----------------------------------------------------------------------------------------------------

# Q6
print("*"* 45 ,"Q6","*"*45)

input = [0, 3, 0, 1, 2, 0, 4]
print(Solutions.move_zeroes(input))
print("\n")

input2 = [0, 1, 0, 3, 6, 0, 0, 0,5]
print(Solutions.move_zeroes(input2))
print("\n")
# ----------------------------------------------------------------------------------------------------

# Q7
print("*"* 45 ,"Q7","*"*45)

input = [10, 20, 40, 30, 40, 20]
print(Solutions.second_largest_distinct_number(input))
print("\n")

input2 = [30, 31, 31, 75, 45, 50]
print(Solutions.second_largest_distinct_number(input2))
print("\n")
# ----------------------------------------------------------------------------------------------------

# Q8
print("*"* 45 ,"Q8","*"*45)

input = [4, 2, 4, 5, 2, 7, 5]


print(Solutions.remove_duplicates(input))
print("\n")

input2 = [1, 4, 3, 4, 2, 0, 3]
print(Solutions.remove_duplicates(input2))

print("\n")
# ----------------------------------------------------------------------------------------------------

# Q9
print("*"* 45 ,"Q9","*"*45)

nums = [1, 2, 4, 5, 6]
print(Solutions.missing_number(nums))
print("\n")

nums2 = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 14]
print(Solutions.missing_number(nums2))

print("\n")
# ----------------------------------------------------------------------------------------------------

# Q10
print("*"* 45 ,"Q10","*"*45)

nums = [2, 7, 11, 15]
target = 9
print(Solutions.find_pair(nums, target))
print("\n")

nums2 = [14, 13, 21, 27]
target2 = 40
print(Solutions.find_pair(nums2, target2))

print("\n")
# ----------------------------------------------------------------------------------------------------

# Q11
print("*"* 45 ,"Q11","*"*45)

input = [-8, -3, 2, 5, -2]
print(Solutions.close_zero(input))
print("\n")

input2 = [-1, -3, 2, 3, -2]
print(Solutions.close_zero(input2))
print("\n")
# ----------------------------------------------------------------------------------------------------

# Q12
print("*"* 45 ,"Q12","*"*45)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(Solutions.common_list_elems(list1, list2))
print("\n")

list3 = [7, 8, 9, 11, 13]
list4 = [13, 12, 8, 11, 14]
print(Solutions.common_list_elems(list3, list4))

print("\n")
# ----------------------------------------------------------------------------------------------------

# Q13
print("*"* 45 ,"Q13","*"*45)

nums = [1, 2, 3, 4, 5]
k = 2
print(Solutions.move_by_k(nums, k))
print("\n")

nums2 = [1, 2, 3, 4, 5, 7, 8, 9]
k2 = 4
print(Solutions.move_by_k(nums2, k2))

print("\n")
# ----------------------------------------------------------------------------------------------------

# Q14
print("*"* 45 ,"Q14","*"*45)

input = [4, 7, 2, 9, 5]
print(Solutions.highest_sum_cons_num(input))
print("\n")

input2 = [1, 8, 3, 4, 6]
print(Solutions.highest_sum_cons_num(input2))

print("\n")
# ----------------------------------------------------------------------------------------------------

# Q15
print("*"* 45 ,"Q15","*"*45)

nums = [2, 4, 3, 5, 7, 8, 1]
target = 9
print(Solutions.unique_pair_sum(nums, target))
print("\n")

nums2 = [9, 4, 8, 10, 7, 3, 12]
target2 = 17
print(Solutions.unique_pair_sum(nums2, target2))

print("\n")