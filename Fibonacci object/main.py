class Fibonacci:
    def __init__(self):
      self.current = 1
      self.previous = None
      self.fib_list = [1]

    def next_fib(self):
      if self.previous == None:
        self.previous = 1
      else:
        self.previous, self.current = self.current, self.previous + self.current
      self.fib_list.append(self.current)

    def prev_fib(self):
      if self.current and self.previous == 1:
        self.previous = None
        self.fib_list.pop()
      elif self.previous == None:
        return 'Impossible'
      else:
        self.previous, self.current = self.current - self.previous, self.previous
        self.fib_list.pop()

    def move_to_N(self, N: int):
      if N > len(self.fib_list):
        while N > len(self.fib_list):
          self.next_fib()
      elif N < len(self.fib_list):
        while N < len(self.fib_list):
          self.prev_fib()
      else:
        pass

    def move_to_n(self, n: int):
      if n > self.current:
        while n > self.current:
          self.next_fib()
      elif n < self.current:
        while n < self.current:
          self.prev_fib()
      else:
        pass

    def dislpay_values(self):
      return fib.current, self.fib_list, len(self.fib_list)
      
        
        

if __name__ == '__main__':
    

  fib = Fibonacci()

  print(fib.current, fib.fib_list)
  fib.next_fib()
  print(fib.dislpay_values())
  fib.next_fib()
  fib.prev_fib()
  fib.prev_fib()
  fib.prev_fib()
  
  print(fib.current, fib.fib_list)
  fib.next_fib()
  print(fib.current, fib.fib_list)
  fib.next_fib()
  print(fib.current, fib.fib_list)
  fib.next_fib()
  print(fib.current, fib.fib_list)
  fib.prev_fib()
  print(fib.current, fib.fib_list)
  fib.next_fib()
  print(fib.current, fib.fib_list)
  fib.next_fib()
  print(fib.current, fib.fib_list)
  fib.next_fib()
  print(fib.current, fib.fib_list)
  fib.move_to_N(7)
  print(fib.current, fib.fib_list)

  fib.move_to_n(1000)
  print(fib.current, fib.fib_list)
