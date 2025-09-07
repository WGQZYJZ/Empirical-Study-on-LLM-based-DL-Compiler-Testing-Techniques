
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        t3 = torch.full([arg1, arg2], 1)
        t4  = torch.cumsum(t3, axis=0) 
        return t4
# Initializing the model
m = Model()
 
# Inputs to the model
args = [5, 6]
__output__  = m(*args)

