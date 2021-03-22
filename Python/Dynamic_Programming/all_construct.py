###################
## All Construct ##
###################
## Problem
# Write a function 'allConstruct(target, wordBank)' that accepts a target string and an array of strings. 
# The function should return a 2D array containing all of the ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array.
# Each element of the 2D array should represent one combination that constructs the 'target'.
# You may reuse elements of 'wordBank' as many times as needed.

### Brute-Force
def all_construct(target, word_bank):
    if target == "":
        return [[]]
    result = []
    for word in word_bank:
        if len(target) >= len(word) and target[: len(word)] == word:
            suffix = target[len(word) :]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [way + [word] for way in suffix_ways]
            if target_ways:
                result.extend(target_ways)
    return result


### Memoized
def all_construct(target, word_bank):
    memo = {}

    def helper(target, word_bank):
        if target == "":
            return [[]]
        if target in memo:
            return memo[target]
        result = []
        for word in word_bank:
            if len(target) >= len(word) and target[: len(word)] == word:
                suffix = target[len(word) :]
                suffix_ways = helper(suffix, word_bank)
                target_ways = [way + [word] for way in suffix_ways]
                if target_ways:
                    result.extend(target_ways)
        memo[target] = result
        return result

    return helper(target, word_bank)


### Tabulation
def all_construct(target, word_bank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]
    for i in range(len(target)):
        for word in word_bank:
            if target[i : i + len(word)] == word:
                new_combinations = [combination + [word] for combination in table[i]]
                table[i + len(word)].extend(new_combinations)
    return table[-1]
