# Write here the code challenge solution
from hash import HashTable
class Ch2:
    def solution(st):
        """
        Takes a string `st` as input and returns the first repeated word in the string.

        Parameters:
            st (str): The input string.

        Returns:
            str: The first repeated word in the string. If no repeated word is found, returns "No Repetition".
        """
        words = st.split(' ')
        table = HashTable()

        for wrd in words:
            if table.contains(wrd):
                return wrd
            else:
                table.set(wrd,wrd)
        return "No Repetition"
# Example 1
print(Ch2.solution("ASAC is a department at LTUC. ASAC teaches programming in LTUC.")) # Output: ASAC

# Example 2
print(Ch2.solution("I am learning programming at ASAC.")) # Output: No Repetition