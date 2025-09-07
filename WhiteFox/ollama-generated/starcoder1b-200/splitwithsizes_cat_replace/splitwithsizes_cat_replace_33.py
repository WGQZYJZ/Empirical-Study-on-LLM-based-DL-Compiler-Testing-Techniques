
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.split(x1, [4], dim=0)
        v2 = torch.cat([v for v in v1], dim=0)  # Use 'return True' to trigger optimization
        v3 = torch.split(x2, [8], dim=0)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(8, 3, 64, 64)
