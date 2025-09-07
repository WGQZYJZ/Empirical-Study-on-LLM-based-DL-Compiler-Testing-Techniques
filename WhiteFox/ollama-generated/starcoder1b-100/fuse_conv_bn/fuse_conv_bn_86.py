
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        self.bn   = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        v1 = self.conv(x)
        return self.bn(v1)

# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(3, 3, 48, 48)
