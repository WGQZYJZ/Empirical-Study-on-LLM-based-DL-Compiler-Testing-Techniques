
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        t1 = torch.addmm(v1, m1, m2) + 1
        v2 = t1.reshape(-1, 3072)
        v3 = nn.functional.normalize(torch.from_numpy(v2))
        return v3

# Initializing the model with specified dim parameter
m = Model(dim=0)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
