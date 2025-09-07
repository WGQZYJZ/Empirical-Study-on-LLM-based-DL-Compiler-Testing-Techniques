
class Model(torch.nn.Module):
    def __init__(self, n1, n2):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v2 * 0.5
        v4 = torch.erf(v3) + 1
        v5 = v2 * v4
        v6 = torch.cat([v1, v2])
        return v6


# Initializing the model
m = Model(n1=32, n2=32)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
