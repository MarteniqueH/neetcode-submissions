class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #Count how many [] / rows are in the entire matrix

        rows = len(matrix)
        
        #Go to the first row / [] in the matrix and count how many values are inside of it 

        columns = len(matrix[0])

        #Set the row pointer at the top row 

        topRow = 0 

        #Set the row pointer at the bottom row 

        bottomRow = rows - 1

        #While the top has not crossed the bottom
        while topRow <= bottomRow:
            #Intitalize the middle Row 

            midRow = (topRow + bottomRow) // 2


            #if the target value is bigger than the last value in the current midRow. Move the mid row down 1 row to a larger row values 

            if target > matrix[midRow][-1]:
                topRow = midRow + 1
            #if the target is smaller that the last value in the current mid row move up to a row above
            elif target < matrix[midRow][0]: 
                bottomRow = midRow - 1

            #if the target row is between the current row this is the row that the target value may be in break out of loop
            else: 
                break 


        #if the top and bottom rows crossed each other then their si not row where the target will exist so return false 

        if not(topRow <= bottomRow):
            return False 


        #now that the correct row has been found the now need to check if the target number is in that range of numbers in the row 


        #find the middle Row
        targetRow = (topRow + bottomRow) // 2

        #Set pointer at the begining of the row 

        left = 0 

        #Set the right pointer at the end of the row
        #columns in the number of values in the row so subracting one puts me at the last index 

        right = columns - 1

        #while left pointer has not crossed the right pinter 

        while left <= right: 
            midInRow = (left + right) // 2

            #if the current mid value in row is greater than the target then the right pointer needs to be shifted in to a smaller value 

            if target < matrix[targetRow][midInRow]:
                right = midInRow - 1
            #if the value in the targetrow is less than the target value then move the left pointer to the next larger number 
            elif target > matrix[targetRow][midInRow]:
                left = midInRow + 1

            #if the number is not smaller or bigger than the target then the target has been found !!! yay
            else : 
                return True
        #if we went through all of the row and do not find the target value return false 
        return False 


                
        