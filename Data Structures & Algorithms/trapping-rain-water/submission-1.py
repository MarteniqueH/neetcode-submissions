class Solution:
    def trap(self, height: List[int]) -> int:
        # If the array is empty, there is no water to trap.
        if not height:
            return 0

        # left starts at the first bar.
        left = 0

        # right starts at the last bar.
        right = len(height) - 1

        # leftMax keeps track of the tallest bar we have seen
        # from the left side.
        leftMax = height[left]

        # rightMax keeps track of the tallest bar we have seen
        # from the right side.
        rightMax = height[right]

        # result stores the total amount of trapped water.
        result = 0

        # Keep working while the two pointers have not crossed.
        while left < right:

            # If the left bar is shorter than the right bar,
            # we process the left side.
            if height[left] < height[right]:

                # Move the left pointer one position to the right.
                left += 1

                # Update leftMax if the new left bar is taller.
                leftMax = max(leftMax, height[left])

                # The amount of water at this position is the
                # difference between leftMax and the current bar.
                result += leftMax - height[left]

            else:
                # Otherwise, we process the right side.

                # Move the right pointer one position to the left.
                right -= 1

                # Update rightMax if the new right bar is taller.
                rightMax = max(rightMax, height[right])

                # The amount of water at this position is the
                # difference between rightMax and the current bar.
                result += rightMax - height[right]

        # Return the total amount of trapped water.
        return result

        