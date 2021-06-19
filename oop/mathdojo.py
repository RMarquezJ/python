import unittest
from unittest import result

class MathDojo:
  def __init__(self):
    self.result=0
  
  def add(self, num, *nums):

    try:
      num=int(num)
      map(int, nums)

    except ValueError:
      return None
    
    self.result+= num

    for i in nums:
      self.result += i
    
    return self

  def subtract(self, num, *nums):

    try:
      num=int(num)
      map(int, nums)

    except ValueError:
      return None
    
    self.result +=num

    for i in nums:
      self.result -= 1

    return self
  
  def standev(self, num, *nums):

    try:
      num=int(num)
      map(int, nums)

    except ValueError:
      return None

    numbers=[num]

    for i in nums:
      numbers.append(i)

    # o numbers=[num] + nums
    
    tot=0
    avg=0
    sumat=0

    for number in numbers:
      tot += number
    print(tot)
    
    avg=tot/len(numbers)
    print(avg)

    for number in numbers:
      sumat += (number-avg)**2
    print(sumat)

    self.result=(sumat/(len(numbers)))**.5
    
    return self

md=MathDojo()


x = md.add(1,2,3,4,5,6).subtract(5,4,3,2,1).result
print(x)

y = md.add(-1,-2,-3,-4,-5).subtract(0,-1,-2,-3,-4).result
print(y)

z = md.add(-2,-1,0,1,2).subtract(-1,-2,-3,-4,-5).result
print(z)

p = md.standev(3,5,7,9).result
print(p)

class MathDojotest(unittest.TestCase):

  def setup(self):
    print('Iniciando prueba de código')

  def testNoStringsAdd(self):
    inp = md.add('uno')
    outp = None
    self.assertEqual(inp,outp)

  def tearDown(self):
    print('Terminando prueba de codigo')

if __name__=='__main__':
  unittest.main()