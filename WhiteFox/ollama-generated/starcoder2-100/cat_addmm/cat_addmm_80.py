

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.addmm(x1, 3., 5.)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
v0 = torch.randn(8, 64)
