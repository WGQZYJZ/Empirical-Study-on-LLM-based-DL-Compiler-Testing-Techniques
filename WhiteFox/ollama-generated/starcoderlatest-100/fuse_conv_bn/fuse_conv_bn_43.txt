
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=3)
        self.bn  = torch.nn.BatchNorm2d(1)

    def forward(self, x1):
        output = self.bn(self.conv(x1))
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 3, 3)
