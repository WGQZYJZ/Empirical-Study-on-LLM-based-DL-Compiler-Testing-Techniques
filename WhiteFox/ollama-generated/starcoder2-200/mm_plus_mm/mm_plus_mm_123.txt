
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, w1, h1):
        v1  = torch.mm(x1, y1) 
        v2  = torch.mm(z1, w1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 80) # This tensor has size [64, 80]
y1 = torch.randn(80, 59) # This tensor has size [80, 59]
z1 = torch.randn(23, 72) # This tensor has size [23, 72]
w1 = torch.randn(72, 44) # This tensor has size [72, 44]
h1 = torch.randn(59, 80) # This tensor has size [59, 80]

