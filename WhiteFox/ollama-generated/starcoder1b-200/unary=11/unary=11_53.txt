
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        return torch.clamp_min(v1, 0), torch.clamp_max(v1, 6), torch.floordiv(v1, 6)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 3, 3)
v1, v2, v3 = m(x1)
