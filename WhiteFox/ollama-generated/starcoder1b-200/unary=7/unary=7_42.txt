
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(32, 16)

    def forward(self, x):
        v = self.conv(x)
        l = self.linear(v)
        l2 = l + 3
        l3 = l2 / 6
        return l3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 14, 14)
