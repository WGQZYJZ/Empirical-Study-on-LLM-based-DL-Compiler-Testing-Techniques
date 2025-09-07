
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).abs()
        v2 = v1 * 0.5
        v3 = v1 * torch.square(v1)
        v4 = torch.cbrt(v3)
        v5 = v4 * 0.044715
        v6 = x1 + v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
