
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
        self.dim = dim
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.cat([v1], self.dim)
        return v3


# Initializing the model
m = Model(0)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
