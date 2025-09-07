
class Model(torch.nn.Module):
    def __init__(self, hidden_dim: int = 512):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 64, 1, stride=1, padding=1)

    def forward(self, x):
        v = torch.cat([
            self.conv1(x),
            self.conv2(x),
        ])
        return v


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(3, 64, 64)
