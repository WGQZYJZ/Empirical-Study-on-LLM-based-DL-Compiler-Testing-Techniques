
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8 * 4 * 4, 16)

    def forward(self, x):
        v = self.conv(x).view(-1, 8, 4, 4)
        v = F.relu(self.linear(v))
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
