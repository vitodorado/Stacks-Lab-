from Stack import Stack
from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    def __init__(self, source, index, new_item):
        super().__init__()
        self.source_list = source
        self.index = index
        self.new_item = new_item
        self.removed_item = None
        

    def execute(self):
        
        #remove the item at the specified index and store it 
        self.removed_item = self.source_list.pop(self.index)
        #Insert the new item at the specified index
        self.source_list.insert(self.index, self.new_item)   
    def undo(self):
        print("Before undo - List:", self.source_list)
        print("Before undo - Removed item:", self.removed_item)
        #remove the new item that was inserted during the execute method
        self.source_list.pop(self.index)
        #reinsert the previously removed item at the original index
        self.source_list.insert(self.index, self.removed_item)
        print("After undo - List:", self.source_list)
      
