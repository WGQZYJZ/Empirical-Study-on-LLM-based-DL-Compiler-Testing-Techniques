
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 4, kernel_size=3)
        self.bn = torch.nn.BatchNorm2d(4)

    def forward(self, x1):
        y1 = self.conv(x1)
        return y1
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 3, 3)
