
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v = self.conv1(x) * 0.5
        v = self.conv2(v) * 0.7071067811865476
        w = torch.erf(v) + 1
        return w

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 3, 64, 64)
