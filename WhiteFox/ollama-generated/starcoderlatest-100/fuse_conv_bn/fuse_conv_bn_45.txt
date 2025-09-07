
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 32, 3)
        self.bn1 = torch.nn.BatchNorm2d(32)
        self.relu = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(32, 64, 3)
        self.bn2 = torch.nn.BatchNorm2d(64)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.bn1(v1)
        v3 = self.relu(v2)
        v4 = self.conv2(v3)
        v5 = self.bn2(v4)

        output = v5

        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
