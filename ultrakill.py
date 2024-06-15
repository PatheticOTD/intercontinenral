def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dick = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    ans = 0
    i = 0
    n = len(s)
    while i < n - 1:
        if (s[i] == 'I') and (s[i+1] in 'VX'):
            ans += roman_dick[s[i+1]] - 1
            i+=2
            if i == (n-1):
                ans += roman_dick[s[i]]
                
        elif (s[i] == 'X') and (s[i+1] in 'LC'):
            ans += roman_dick[s[i+1]] - 10
            i+=2
            if i == (n-1):
                ans += roman_dick[s[i]]
        elif (s[i] == 'C') and (s[i+1] in 'DM'):
            ans += roman_dick[s[i+1]] - 100
            i+=2
            if i == (n-1):
                ans += roman_dick[s[i]]
        else:
            ans+= roman_dick[s[i]]
            i+=1
            if (i + 1) == n:
                ans += roman_dick[s[i]]
                break
                
            
    return ans

string = 'MDCXCV'
print(romanToInt(string))