
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2  = torch.cat([v1] * len(range(0,3))) # Replace the length of the list in range(0,3) by the length of the concatenation dimension, and concatenate along dim=4
        return v2


# Initializing the model
m  = Model()
 

# Inputs to the model
x1  = torch.randn(875, 64)
x2  = torch.randn(903, 64)
 
__output__  = m(x1, x2)
