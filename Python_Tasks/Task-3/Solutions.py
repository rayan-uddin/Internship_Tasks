# Q1
def count_of_words(self):
    words = self.split()

    words_dict = dict()
    for i in words:
        count = 0
        for j in words:
            if i == j:
                count += 1
                words_dict[i] = count

    return words_dict

# Q2

def count_of_chars(self):
    chars_dict = dict()
    for i in self:
        count = 0
        for j in self:
            if i == j:
                count += 1
                chars_dict[i] = count

    return chars_dict

# Q3

def appears_once_word(self):
    for i in self:
        count = 0

        for j in self:
            if i.lower() == j.lower():
                count += 1

        if count == 1:
            return i

    return None

# Q4

def check_anagram(char1, char2):
    word1 = count_of_chars(char1)
    word2 = count_of_chars(char2)
    return word1 == word2

# Q5

def second_occurence(word):

    for i in word:
        count = 0

        for j in word:
            if i.lower() == j.lower():
                count += 1

            if count == 2:
                return i

    return None

# Q6

def move_zeroes(l1):
    
    i = 0
    l2 = []
    while i < len(l1):
        if l1[i] == 0:
            l2.append(l1[i])
            del l1[i]
        else:
            i += 1
    l1.extend(l2)
    return l1

# Q7 

def second_largest_distinct_number(l1):
    i = 0
    unique_number = []

    while i < len(l1):
        if l1[i] not in unique_number:
            unique_number.append(l1[i])
        else:
            i += 1

    if len(unique_number) == 1:
        return None

    unique_number.sort()

    second_largest_number = unique_number[1]
    
    return second_largest_number

# Q8

def remove_duplicates(l1):
    i = 0
    unique_list = []
    while i < len(l1):
        if l1[i] not in unique_list:
            unique_list.append(l1[i])
        else:
            i += 1

    return unique_list

# Q9

def missing_number(nums):
        for i in range(1, max(nums) + 1):
            if i not in nums:
                return i

            
# Q10

def find_pair(list, number):

    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j]:
                return [list[i], list[j]]


# Q11


def close_zero(l):
    
    closest = l[0]
    
    for i in l:
        if abs(i) < abs(closest):
            closest = i
        elif abs(i) == abs(closest) and i > closest:
            closest = i
    
    return closest

# Q12

def common_list_elems(list1, list2):
    common_elems = []
    
    for i in list1:
        for j in list2:
            if j == i:
                common_elems.append(i)
    return common_elems

# Q13

def move_by_k(list, k):
    n = len(list)
    k = k % n
    result = []
    
    for i in range(n):
        result.append(list[(i - k) % n])
    
    return result

# Q14

def highest_sum_cons_num(list):
    highest_sum = 0
    for i in range(len(list) - 1):
        if int(list[i]) + int(list[i+1]) > highest_sum:
            highest_sum = int(list[i]) + int(list[i + 1])
    
    return highest_sum

# Q15

def unique_pair_sum(nums, target):
    sequences = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])
                sequences.append(pair)

    sequences.sort(key = lambda x: x[0])
    return sequences