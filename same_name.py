"""This is SameName.py"""
def spam():
    """This is spam method"""
    eggs = 'spam local'
    print(eggs)#'spam local'を表示

def bacon():
    """This is bacon method"""
    eggs = 'bacon local'
    print(eggs)#'bacon local'を表示
    spam()
    print(eggs)#'bacon local'を表示

EGGS = 'global'
bacon()
print(EGGS)#'global'を表示
