S = 'dvdf'

def longestuniquestring(sentence):
    hashmap = {}
    maxunique = 0
    left = 0
    # for all letters in sentence
    for i in range(len(sentence)):
        # if letter not in hashmap add it and increment maxunique
        if sentence[i] not in hashmap:
            hashmap[sentence[i]] = 1
            maxunique += 1
            maxunique = max(maxunique, (i - left +1))
            print(maxunique)
        if sentence[i] in hashmap:
            #if letter in hashmap set left = to letter index + 1
            hashmap[sentence[i]] = i
            left = i + 1
    return maxunique

print(longestuniquestring(S))
