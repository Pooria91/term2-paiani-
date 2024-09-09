

import random
import turtle as t

class Robot:
   def __init__(self):
       self.history = []

   def seve_history(self, filename):
       with open(filename, 'w')as file:
           for item in self.history:
               file.write(str(item) + '\n')


   def load_history(self, filename):
       with open(filename, 'r') as file:
           self.history = [line.strip() for line in file]


   def random_operation(self):
       operations = ['Addition', 'subtracition', 'Multiplication', 'Division']
       operation = random.choice(operations)
       return operation


   def run(self):
       while True:
           operation = self.random_operation() 
           print(f'operation:{operation}')
           num1 = int(input('Enter the first nuber: '))
           num2 = int(input('Enter the second number: '))
           if operation == 'Addtion':
               result = num1 + num2   
           elif operation == 'subtracition':
               result = num1 - num2
           elif operation == 'Multiplication':
               result = num1 * num2
           elif operation == 'Division':
               result = num1 / num2
           self.history.append(f'{num1} {operation} {num2} = {result}')
           print(f'Result: {result}')
           choice = input('Do you want to continuo?')
           if choice.lower() != 'y':
               self.seve_history('history.txt')
               break


class colorfulshope:
   def __init__(self, sides, lenget, color = None):
       self.sides = sides
       self.lenget = lenget
       self.color = color

   def draw(self):
       t.color(self.color)
       for _ in range(self.sides):
           t.forward(self.lenget)
           t.right(360 / self.sides)

robot = Robot()
robot.run()

shape1 = colorfulshope(5, 100, 'red')
shape1.draw


t.done()
