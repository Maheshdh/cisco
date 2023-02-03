def is_pal(s):
  return s==s[::-1]

def double_base_palindromes(n):
  ans = 0
  for i in range(1,n+1):
    if is_pal(str(i)) and is_pal(bin(i)[2:]):
      ans+=i
  return ans

double_base_palindromes(3)
