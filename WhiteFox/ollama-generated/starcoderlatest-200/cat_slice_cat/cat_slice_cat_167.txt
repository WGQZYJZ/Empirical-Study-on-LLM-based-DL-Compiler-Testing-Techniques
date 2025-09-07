
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v1 = torch.cat([x, x], dim=1)
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(20, 3, 64, 64)
