
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.relu  = torch.nn.LeakyReLU()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.relu(v1) * 0.5
        v3 = v1 * (0.7071067811865475 + 1j) * negative_slope
        v4 = torch.where(torch.abs(v2) > threshold, x1 * (negative_slope + 1j), v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
