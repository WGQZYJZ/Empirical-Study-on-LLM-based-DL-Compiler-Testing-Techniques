
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2, z3, z4):
        v1  = torch.mm(x1, y2) 
        v2  = torch.mm(z3, z4)  
        return v1 + v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(6000, 50)
y1  = x1.t().clone() * 0.793854242
z1  = y1.t().clone() + 1j * -12.4677892e-17
z2  = torch.zeros_like(y1) + 157.80303955078125  # A constant that is not a matrix of 0s and 1s
