
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, [2, 3], dim=1)
        v2 = torch.cat([v1[0], v1[1]], dim=1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 3, 64, 64)
