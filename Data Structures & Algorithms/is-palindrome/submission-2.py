class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Set left pointer to the beginning of the string
        left = 0

        # Set right pointer to the end of the string
        right = len(s) - 1

        # Continue checking characters while the pointers haven't crossed
        while left < right:
            # Move left forward until we find an alphanumeric character
            while left < right and not self.alphaNum(s[left]):
                left += 1

            # Move right backward until we find an alphanumeric character
            while right > left and not self.alphaNum(s[right]):
                right -= 1

            # Compare the characters in lowercase
            if s[left].lower() != s[right].lower():
                # If they don't match, the string is not a palindrome
                return False

            # Move both pointers toward the center
            left += 1
            right -= 1

        # If all characters matched, the string is a palindrome
        return True

    # Helper function to check whether a character is alphanumeric
    def alphaNum(self, c):
        # Return True if c is an uppercase letter
        return (
            ord('A') <= ord(c) <= ord('Z')
            # Or if c is a lowercase letter
            or ord('a') <= ord(c) <= ord('z')
            # Or if c is a number
            or ord('0') <= ord(c) <= ord('9')
        )