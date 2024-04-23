import sys
class Args:
    def __init__(self):
        self.args = sys.argv
    
    def flag(self, flag_name: str) -> bool:
        return flag_name in self.args
