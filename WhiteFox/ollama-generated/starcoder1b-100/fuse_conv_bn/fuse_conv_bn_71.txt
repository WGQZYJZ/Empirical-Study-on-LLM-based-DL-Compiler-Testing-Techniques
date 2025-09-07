
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2 or 3 representing the number of channels
        self.bn = torch.nn.BatchNorm2d(...)  # X should match with Conv2d
        self.relu = torch.nn.ReLU(inplace=True)

    def forward(self, x):
        output = self.conv(x)
        output = self.bn(output)
        output = self.relu(output)

        return output


# Inputs to the model
x1 = torch.randn(...)  # 2 or 3 dimension input
