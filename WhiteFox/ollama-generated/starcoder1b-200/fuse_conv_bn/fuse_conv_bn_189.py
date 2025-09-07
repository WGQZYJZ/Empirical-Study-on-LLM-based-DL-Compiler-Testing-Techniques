
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)  # X can be 1, 2 or 3 representing the dimension
        self.conv2 = torch.nn.Conv2d(...)  # X can be 1, 2 or 3 representing the dimension
        self.bn   = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        output = self.conv1(x)
        output = self.conv2(output)
        output = self.bn(output)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 4, 4)
