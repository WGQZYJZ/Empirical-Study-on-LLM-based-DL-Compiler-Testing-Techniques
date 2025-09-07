
class Model(torch.nn.Module):
    def __init__(self, n_channels=3, n_features=8, kernel_size=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(n_channels, n_features, kernel_size)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
