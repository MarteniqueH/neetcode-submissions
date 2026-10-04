class Solution:
    from collections import defaultdict; 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #find strings that have the same number of the same letter and group them into a sub array together and the return all those sub arrays into one 

        #input string array 
        #process find all the strings that have the same letters and the same  number of occurances in the strigs 
        #return large string with substrings of the group anagrams 

        '''
        1. use a dictrionary to create key value pairs for each of the distinct groups of letters

        2. for each word if that order of letters is not already in the dictionary add it as a key 
        3. If the group of letters. already exist in the array the just add it as a value in that dictionary postision

        '''

        
        store = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))

            store[key].append(word)

        return list(store.values())

        
        