
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.mat = torch.nn.Parameter(torch.randn(dim))
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat, self.mat)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model(256)

# Inputs to the model
x1 = torch.randn(32, 3, 64, 64)
