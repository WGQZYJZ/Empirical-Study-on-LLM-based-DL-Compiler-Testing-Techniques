
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        output = self.conv(x1)
        output = self.bn(output)
        return output


# Initializing the model
m = Model()


