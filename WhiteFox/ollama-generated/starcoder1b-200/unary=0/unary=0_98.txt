
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(1, -1) ** 2
        v2 = v1 * 0.5
        v3 = torch.pow(v1, 3) * 0.044715
        v4 = torch.cat([v2, v3], dim=1) + 1
        v5 = torch.tanh(v4).view(1, -1) ** 0.7978845608028654
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
