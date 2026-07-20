class Solution:

    def encode(self, strs: List[str]) -> str:
        #This will store the final encoded string 
        result = ""
        #Loop through each string in the list one at a time 
        for s in strs: 
            #Add the length of the string, seperate with (#), then the actual string 
            result += str(len(s)) + "#" + s
        #Return the completed encdoed string 
        return result

    def decode(self, s: str) -> List[str]:
        #Result will store the decoded words 
        #i is the starting postion while reading the string 
        result, i = [], 0
        #keep going until the entire string has been checked 
        while i < len(s):
            #j will move forward to find the "#"
            j = i
            #Move j until it finds the "#"
            #The numbers before "#" is the length of ther string 
            while s[j] != "#":
                j += 1

            #convert the characters before the "#" into numbers
            length = int(s[i:j])
            #Get the acutal word after "#"
            #j +1 starts after the "#"
            #j + 1 + length denotes where he word ends 
            result.append(s[j + 1 : j + 1 + length])
            #Move i to the bengining of the next encoded word 
            i = j + 1 + length 
        #return the list of decoded string 
        return result
