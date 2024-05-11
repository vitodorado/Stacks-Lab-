from Stack import Stack
from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    def __init__(self, source, index, new_item):
        super().__init__()
        self.source_list = source
        self.index = index
        self.new_item = new_item
        

    def execute(self):
        #insert the new item at the specified index 
        self.source_list.insert(self.index, self.new_item)
    def undo(self):
        del self.source_list[self.index]    
      
      
