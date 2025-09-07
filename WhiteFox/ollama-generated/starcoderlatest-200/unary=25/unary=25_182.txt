
class Model(torch.nn.Module):
    def __init__(self, n_classes=10, negative_slope=0.02):
        super().__init__()
        self.conv = torch.nn.Linear(64 * 64 * 3, 10)

    def forward(self, x1):
        v1 = torch.reshape(x1, (1,-1))
        v2 = self.conv(v1)
        v3 = torch.where(v2 > 0, v2, -self.conv * negative_slope)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 64, 3)
