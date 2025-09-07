
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.linear = torch.nn.Linear(64 * 64, 64 * 64)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.linear(v1)
        return torch.clamp_min(v2 + 3, 0), torch.clamp_max(v2 / 6, 6)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
