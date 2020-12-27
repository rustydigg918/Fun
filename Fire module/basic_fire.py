# # Snipp -1 >>>
# import fire

# class Calculator(object):

#   def add(self, x, y):
#     return x + y

#   def multiply(self, x, y):
#     return x * y

# if __name__ == '__main__':
#   calculator = Calculator()
#   fire.Fire(calculator)

# # Snipp -2 >>>
# import fire

# def add(x, y):
#   return x + y

# def multiply(x, y):
#   return x * y

# if __name__ == '__main__':
#   fire.Fire({
#       'sum': add,
#       'product': multiply,
#   })

# # Snipp -3 >>>
# import fire

# def add(x, y):
#   return x + y

# def multiply(x, y):
#   return x * y

# if __name__ == '__main__':
#   fire.Fire()

# # Snipp -4 >>>
# import fire

# class Calculator(object):

#   def add(self, x, y):
#     return x + y

#   def multiply(self, x, y):
#     return x * y

# if __name__ == '__main__':
#   fire.Fire(Calculator)

# >>> Broken Calculator <<<
import fire

class BrokenCalculator(object):

  def __init__(self, offset=1):
      self._offset = offset

  def add(self, x, y):
    return x + y + self._offset

  def multiply(self, x, y):
    return x * y + self._offset

if __name__ == '__main__':
  fire.Fire(BrokenCalculator)