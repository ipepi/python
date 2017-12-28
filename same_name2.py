"""This is SameName2.py"""
def spam():
    """This is spam method"""
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
