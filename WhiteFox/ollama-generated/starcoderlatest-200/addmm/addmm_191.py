
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp=None):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 64) # shape: (32, 64)
x2 = torch.randn(64, 32) # shape: (64, 32)
inp = torch.randn(32)     # shape: (32,)
