
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2 = torch.nn.Conv2d(8, 16, 4)

    def forward(self, x1, x2):
        v1 = self.conv1(x1) * 0.5
        v2 = self.conv2(v1) * 0.7071067811865476
        v3 = torch.cat([v2, x2], dim=1)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(2, 16, 64, 64)
