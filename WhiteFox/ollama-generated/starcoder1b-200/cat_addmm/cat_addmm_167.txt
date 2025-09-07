
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.bn1  = torch.nn.BatchNorm2d(8)
        self.relu1 = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(8, 16, 3)
        self.bn2  = torch.nn.BatchNorm2d(16)
        self.conv3 = torch.nn.Conv2d(16, 1, 1)

    def forward(self, x):
        x0 = self.relu1(self.bn1(self.conv1(x)))
        return self.conv2(torch.cat([x0, x], dim=1))


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
