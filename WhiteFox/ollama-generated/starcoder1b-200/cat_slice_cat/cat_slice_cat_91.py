
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1[:, 0:9223372036854775807] * 0.5
        v3 = v1[:, 0:size] * 0.7071067811865476
        v4 = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
