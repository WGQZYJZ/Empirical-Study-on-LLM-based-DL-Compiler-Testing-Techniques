
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v1 = torch.full([arg1, arg2], 1) 
        return torch.cumsum(v1, 1).int()


# Initializing the model
m  = Model()


# Inputs to the model
arg1  = 345
arg2  = 7890
 
__output__  = m(arg1, arg2)

