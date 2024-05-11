from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    def __init__(self, source, index1, index2):
        super().__init__()
        self.source_list = source
        self.index1 = index1
        self.index2 = index2
        self.old_value1 = self.source_list[index1]
        self.old_value2 = self.source_list[index2]
        

    def execute(self):
        #backup the original state of the list
        self.items_backup = self.source_list[:]
        #swap items at index1 and index2
        self.source_list[self.index1], self.source_list[self.index2] = self.source_list[self.index2], self.source_list[self.index1]
    
    def undo(self):
        self.source_list[self.index1] = self.old_value1
        self.source_list[self.index2] = self.old_value2