
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dim = dim
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.cat([v1], dim=self.dim)
        return v2


# Initializing the model
m = Model(dim=0)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
