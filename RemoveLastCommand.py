from UndoCommand import UndoCommand

class RemoveLastCommand(UndoCommand):
    def __init__(self, source):
        super().__init__()
        self.source_list = source

    def execute(self):
        if self.source_list:
            #remove the last item if the list is not empty
            removed_item = self.source_list.pop()
            return removed_item
        else:
            return None #return None if the list is empty 
