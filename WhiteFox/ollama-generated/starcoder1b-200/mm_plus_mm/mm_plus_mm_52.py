
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4, x5, x6, x7):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        v4 = torch.mm(x5, x6)  # Matrix multiplication between input5 and input6
        v5 = torch.mm(x7, x8)  # Matrix multiplication between input7 and input8
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 4, 64, 64)
x3  = torch.randn(1, 8, 64, 64)
x4  = torch.randn(1, 5, 64, 64)
x5  = torch.randn(1, 6, 64, 64)
x6  = torch.randn(1, 7, 64, 64)
x7  = torch.randn(1, 8, 64, 64)
