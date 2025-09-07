
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * (v1 * 0.5)
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return self.conv2(v6)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 32, 64)
