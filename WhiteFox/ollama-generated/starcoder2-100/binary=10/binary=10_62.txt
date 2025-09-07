
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): # Note that "other" has not been defined yet!
        v1 = self.linear(x1) + self.__other__ # This will fail to compile
        return v1
 

class Model_2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2): # Note that "other" has been defined!
        v1 = self.linear(x2) + self.__other__ 
        return v1
