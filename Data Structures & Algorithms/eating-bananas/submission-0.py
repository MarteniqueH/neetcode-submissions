class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #left is the smallest possible speed
        left = 1
        #the largest possible speed
        right = max(piles)
        #Keeps track of the best answer seen so far 
        #This is intilized with the max speed so the largest number in the list of piles
        result = right
        
        #Keep searching as long there are still possible speeds to investigate
        while left <= right:
            #Find the middle speed 

            k = (left + right) // 2
            
            #Now calculate how many total hours koko needs if she eats a the k speed
            #initalize to zero becuase not piles have beem looked at yet. 
            totalTime = 0

            #Go through all the piles one at a time 

            for pile in piles:
                # p / k is how many hours the pile would take mathmatically
                #math.ceil rounds the number up to the nearest whole number 
                #totalTime + addes the hours to the total tile. 

                totalTime += (pile + k - 1)// k
        #Can koko finished all the bananas within the allowed number of hours.
        #If the answer is. yes then the. speed works

            if totalTime <= h:
                #Save this speed as current answer
                result = k
                right = k - 1
            else:
                left = k + 1
        return result

        