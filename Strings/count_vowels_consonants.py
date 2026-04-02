def count_vowels_consonants(s):
    vowels='aeiouAEIOU'
    vowels_count=0
    consonants_count=0
    
    for char in s.lower():
        if char.isalpha():
            if char in vowels:
                vowels_count+=1
            else:
                consonants_count+=1
    return vowels_count,consonants_count
v,c=count_vowels_consonants("Hello World!")
print("vowerls:",v)
print("consonants:",c)
