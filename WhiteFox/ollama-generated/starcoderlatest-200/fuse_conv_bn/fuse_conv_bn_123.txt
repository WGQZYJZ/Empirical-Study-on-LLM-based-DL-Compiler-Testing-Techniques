
class Model(torch.nn.Module):
    def __init__(self, kernel_size=3):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        output = self.conv(x) # This line is replaced with a call to `torch.nn.functional.conv2d`
        return self.bn(output)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 8, 8)
