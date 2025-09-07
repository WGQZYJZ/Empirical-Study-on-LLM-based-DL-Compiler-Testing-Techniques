
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat([x2, x3], dim=0)
        return v1[:, 4611686018427387905]


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(25, 32, 16)
x3 = torch.randn(23, 32, 16)
