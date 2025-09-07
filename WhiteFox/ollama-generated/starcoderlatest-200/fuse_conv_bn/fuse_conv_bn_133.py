
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        conv = self.conv(x1)
        bn = self.bn(conv)
        output = self.conv + bn
        return output

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 2, 3, 3)
