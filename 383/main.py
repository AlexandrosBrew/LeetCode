ransomNote = input('Ransome Note = ')
magazine = input('Magazine = ')

def canConstruct(ransomNote, magazine):
    mag_freq = {}
    for char in magazine:
        mag_freq[char] = mag_freq.get(char, 0) +1
    
    for char in ransomNote:
        if char not in mag_freq or mag_freq[char] == 0:
            return False
        mag_freq[char] -= 1
    return True

print(canConstruct(ransomNote, magazine))

#!Completed!