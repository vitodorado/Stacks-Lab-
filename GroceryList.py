from Stack import Stack
from InsertAtCommand import InsertAtCommand
from RemoveLastCommand import RemoveLastCommand
from SwapCommand import SwapCommand

class GroceryList:
    def __init__(self):
        self.list_items = []
        self.undo_stack = Stack()
        self.add_with_undo("chips")
        self.add_with_undo("cookies")
        self.add_with_undo("waffles")
        self.add_with_undo("syrup")
        self.add_with_undo("ice cream")
        self.add_with_undo("lettuce")

    def add_with_undo(self, new_item_name):
        # Add the list item
        self.list_items.append(new_item_name)

        # Make an undo command that removes the last item and pushes it onto the undo stack
        self.undo_stack.push(RemoveLastCommand(self.list_items))

    def remove_at_with_undo(self, removal_index):
        #check if index is valid
        if 0 <= removal_index < len(self.list_items):
            #store the removed item
            removed_item = self.list_items[removal_index]
            #remove the item at the specified index
            del self.list_items[removal_index]

            #push an InsertAtCommnad onto the undo stack to undo the removal
            insert_command = InsertAtCommand(self.list_items[:], removal_index, removed_item)
            self.undo_stack.push(insert_command)
        
            
        

    def swap_with_undo(self, index1, index2):
        self.items_backup = self.list_items[:]
        #create a swap command object
        swap_command = SwapCommand(self.list_items, index1, index2)
        #execute the swap operation 
        swap_command.execute()
        #push the swap command onto the undo stack to undo the swap
        self.undo_stack.push(swap_command)
        

        

        
    
        
        
        

    def execute_undo(self):
       if self.undo_stack:
           #pop the last command from the undo stack
           undo_command = self.undo_stack.pop()
            #Check if the undo command is an instance of RemoveLastCommand
           if isinstance(undo_command, RemoveLastCommand):
               #execute the undo command
               undo_command.execute()
           elif isinstance(undo_command, SwapCommand):
               undo_command.undo()
           elif isinstance(undo_command, InsertAtCommand):
               undo_command.undo()
               
           

    def get_list_size(self):
       return len(self.list_items)

    def get_undo_stack_size(self):
       return self.undo_stack.size()

    def get_list_copy(self):
       return self.list_items[:]

    def print_list(self, outfil):
        for n, item in enumerate(self.list_items):
            print(f"""{n}. {item}""", file=outfil)
