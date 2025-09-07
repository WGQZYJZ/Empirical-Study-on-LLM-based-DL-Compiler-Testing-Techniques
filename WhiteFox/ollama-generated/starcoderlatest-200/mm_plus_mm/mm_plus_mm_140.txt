
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 32, 3, stride=1, padding=0)

    def forward(self, x1, x2, x3, x4, x5, x6):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
x3 = torch.randn(1, 4, 64, 64)
x4 = torch.randn(1, 2, 64, 64)
x5 = torch.randn(1, 1, 64, 64)
x6 = torch.randn(1, 800, 64, 64)
