

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + v1
        v4 = torch.relu(v2)
        return v4


m  = Model()
x1 = torch.randn(1, 3, 64, 64)
