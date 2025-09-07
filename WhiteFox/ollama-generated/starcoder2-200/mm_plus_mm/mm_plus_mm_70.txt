
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1):
        v1  = torch.mm(x1, y1) # Matrix multiplication between input1 and input2
        v2  = torch.mm(y1, z1) # Matrix multiplication between input3 and input4
        v3  = v1 + v2          # Addition of the results of the two matrix multiplications
        return v3

# Initializing the model
m = Model()

# Inputs to the model
i1  = torch.randn(5, 6)
i2  = torch.randn(7, 8)
i3  = torch.randn(4, 9)
i4  = torch.randn(7, 5)
__output__  = m(i1, i2, i3)

