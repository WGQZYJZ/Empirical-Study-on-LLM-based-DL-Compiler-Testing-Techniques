
class Model(torch.nn.Module):
    def __init__(self, dim: int = 2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 7)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1 for _ in range(dim)], dim=dim)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
