'''
main.py
'''
# dunder or magic methods
from todo import Todo

k_todo = Todo(name='Kingsley')
e_todo = Todo(name='Emmanuel')

k_todo.add('buy milk')

e_todo.add('wake up')
e_todo.add('code')

'''
todo.py
'''
class Todo:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    # referenced by programmers
    def __repr__(self):
        return f"{__class__.__name__}('{self.name}')"
    
    # referenced by users
    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.items)
    
    def __gt__(self, other):
        return len(self.items) > len(other.items)
    
    def __lt__(self, other):
        return len(self.items) < len(other.items)