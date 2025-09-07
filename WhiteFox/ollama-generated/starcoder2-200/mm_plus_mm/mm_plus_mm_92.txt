
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2, z3, u4):
        v1 = torch.mm(x1, y2) # Matrix multiplication between input1 and input2
        v2 = torch.mm(z3, u4) # Matrix multiplication between input3 and input4
        v3  = v1 + v2 # Addition of the results of the two matrix multiplications 
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1   = torch.randn(6,8)
y2  = torch.randn(4,8)
z3    = torch.randn(5,7)
u4 = torch.randn(8,9)

__output__= m(x1, y2, z3, u4)

