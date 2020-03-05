class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
        i = 0
        a = 0
        while(i < len(bits)):
            if bits[i] == 0:
                a = 1
            else:
                a = 2
            i += a
        if a == 1:
            return True
        else:
            return False
