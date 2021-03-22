#####################
## Count Construct ##
#####################
## Problem
# Write a function 'countConstruct(target, wordBank)' that accepts a target string and an array of strings. 
# The function should return the number of ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array.
# You may reuse elements of 'wordBank' as many times as needed.

### Brute-Force
def count_construct(target, word_bank):
    if target == "":
        return 1
    totalCount = 0
    for word in word_bank:
        if len(target) >= len(word) and target[: len(word)] == word:
            remainder = target[len(word) :]
            totalCount += count_construct(remainder, word_bank)
    return totalCount


### Memoized
def count_construct(target, word_bank):
    memo = {}

    def helper(target, word_bank):
        if target == "":
            return 1
        if target in memo:
            return memo[target]
        totalCount = 0
        for word in word_bank:
            if len(target) >= len(word) and target[: len(word)] == word:
                remainder = target[len(word) :]
                totalCount += helper(remainder, word_bank)
        memo[target] = totalCount
        return totalCount

    return helper(target, word_bank)


### Tabulation
def count_construct(target, word_bank):
    table = [0] * (len(target) + 1)
    table[0] = 1
    for i in range(len(target)):
        if table[i]:
            for word in word_bank:
                if target[i : i + len(word)] == word:
                    table[i + len(word)] += table[i]
    return table[-1]
