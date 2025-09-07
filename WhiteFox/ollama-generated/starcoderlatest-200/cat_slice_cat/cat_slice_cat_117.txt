
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = v6[:, :, :size, :size] # Further slice the tensor along dimension 1
        return torch.cat([v1, v7], dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(2, 32, 32)
