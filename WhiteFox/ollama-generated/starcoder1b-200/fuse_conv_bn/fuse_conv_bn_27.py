
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        self.bn  = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        output = self.bn(self.conv(x))

# Initializing the model
m  = Model()

 # Inputs to the model
x  = torch.randn(1, 1, 3, 3)
