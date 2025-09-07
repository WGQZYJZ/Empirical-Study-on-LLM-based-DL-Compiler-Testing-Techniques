
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, 4)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        output = self.conv(x1).relu_() + self.bn(x1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2, 2)
