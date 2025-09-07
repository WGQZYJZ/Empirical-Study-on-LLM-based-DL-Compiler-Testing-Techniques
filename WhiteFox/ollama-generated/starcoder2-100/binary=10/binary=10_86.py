
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1,8)
 
    def forward(self, x2):
        v2  = self.linear(x2)+ self.__input__
        return v5


# Initializing the model