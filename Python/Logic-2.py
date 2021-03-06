# Logic-2

def make_bricks(small, big, goal):
  big *= 5
  if big == goal:
    return True
  if small == goal:
    return True
  if big % goal + small >= goal:
    return True
  if 5 + small >= goal and big > 0:
    return True
  if 10 + small == goal and big > 1:
    return True
  
  return False

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c) 
def fix_teen(n):
  if n > 10 and n < 20:
    if n == 15 or n == 16:
      return n
    else:
      return 0
  else:
    return n

def lone_sum(a, b, c):
  if(a==b and b==c):
    return 0
  if(a==b):
    return c
  if(b==c):
    return a
  if(c==a):
    return b
  
  return a+b+c

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  return a + b + c

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
def round10(num):
  if num > 10:
    if num % 10 >= 5:
      st = str(num)
      st = st[0] + '0'
      return int(st) + 10
    else:
      st = str(num)
      st = st[0] + '0'
      return int(st)
  else:
    if num >= 5:
      return 10
    else:
      return 0
    
def close_far(a, b, c):
  if(abs(a - b) >= 2 and abs(b - c) >= 2 and abs(a - c) <= 1):
    return True
  elif(abs(a - c) >= 2 and abs(b - c) >= 2 and abs(a - b) <= 1):
    return True
  else:
    return False
