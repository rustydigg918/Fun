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

# # >>> Broken Calculator <<<
# import fire

# class BrokenCalculator(object):

#   def __init__(self, offset=1):
#       self._offset = offset

#   def add(self, x, y):
#     return x + y + self._offset

#   def multiply(self, x, y):
#     return x * y + self._offset

# if __name__ == '__main__':
#   fire.Fire(BrokenCalculator)

# # >>> Grouping Commands <<<
# import fire
# class IngestionStage(object):
    
#   def run(self):
#     return 'Ingesting! Nom nom nom...'

# class DigestionStage(object):

#   def run(self, volume=1):
#     return ' '.join(['Burp!'] * volume)

#   def status(self):
#     return 'Satiated.'

# class Pipeline(object):

#   def __init__(self):
#     self.ingestion = IngestionStage()
#     self.digestion = DigestionStage()

#   def run(self):
#     self.ingestion.run()
#     self.digestion.run()

# if __name__ == '__main__':
#   fire.Fire(Pipeline)

# # Accessing Properties >>> 

# from airports import airports

# import fire

# class airport(object):

#   def __init__(self, code):
#     self.code = code
#     self.name = dict(airports).get(self.code)
#     self.city = self.name.split(',')[0] if self.name else None

# if __name__ == '__main__':
#   fire.Fire(Airport)

# # Chaining Function Calls
# import fire

# class BinaryCanvas(object):
#   """A canvas with which to make binary art, one bit at a time."""

#   def __init__(self, size=10):
#     self.pixels = [[0] * size for _ in range(size)]
#     self._size = size
#     self._row = 0  # The row of the cursor.
#     self._col = 0  # The column of the cursor.

#   def __str__(self):
#     return '\n'.join(' '.join(str(pixel) for pixel in row) for row in self.pixels)

#   def show(self):
#     print(self)
#     return self

#   def move(self, row, col):
#     self._row = row % self._size
#     self._col = col % self._size
#     return self

#   def on(self):
#     return self.set(1)

#   def off(self):
#     return self.set(0)

#   def set(self, value):
#     self.pixels[self._row][self._col] = value
#     return self

# if __name__ == '__main__':
#   fire.Fire(BinaryCanvas)

# # Even Simpler >>>
# import fire
# english = 'Hello World'
# spanish = 'Hola Mundo'
# fire.Fire()

# # Calling Functions >>>
# import fire

# class Building(object):

#   def __init__(self, name, stories=1):
#     self.name = name
#     self.stories = stories

#   def climb_stairs(self, stairs_per_story=10):
#     for story in range(self.stories):
#       for stair in range(1, stairs_per_story):
#         yield stair
#       yield 'Phew!'
#     yield 'Done!'

# if __name__ == '__main__':
#   fire.Fire(Building)

# Functions with *varargs and **kwargs >>>
import fire

def order_by_length(*items):
  """Orders items by length, breaking ties alphabetically."""
  sorted_items = sorted(items, key=lambda item: (len(str(item)), str(item)))
  return ' '.join(sorted_items)

if __name__ == '__main__':
  fire.Fire(order_by_length)