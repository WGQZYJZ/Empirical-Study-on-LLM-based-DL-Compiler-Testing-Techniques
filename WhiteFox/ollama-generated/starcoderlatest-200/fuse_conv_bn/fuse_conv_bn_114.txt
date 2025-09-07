
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # input channel is 3 and output channel is 2
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        v1 = self.conv(x1)
        return self.bn(v1)

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 32, 32)
