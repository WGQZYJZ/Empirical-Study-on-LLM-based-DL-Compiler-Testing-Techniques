
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 3, kernel_size=3)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        output = self.conv(x1).permute(0, 2, 3, 1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4, 4)
