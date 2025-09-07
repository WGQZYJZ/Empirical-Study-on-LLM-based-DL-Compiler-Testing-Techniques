
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2, z3):
        v1  = torch.mm(x1, y2) # Matrix multiplication between input1 and input2
        v2  = torch.mm(z3, 400.) # Matrix multiplication with constant
        v3  = v1 + v2 
        return v3


# Initializing the model
m  = Model() 


# Inputs to the model
x1  = torch.randn(8, 8)
y2  = torch.randn(7, 6)
z3  = torch.randn(50,)
__output__  = m(x1, y2, z3)

