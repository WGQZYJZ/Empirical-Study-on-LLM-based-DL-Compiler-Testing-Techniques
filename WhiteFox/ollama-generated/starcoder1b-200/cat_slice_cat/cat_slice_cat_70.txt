
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        t = torch.cat([x1, x2, x3], dim=1)
        return t

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 3, 10, 10)
x3 = torch.randn(1, 1, 10, 10)
