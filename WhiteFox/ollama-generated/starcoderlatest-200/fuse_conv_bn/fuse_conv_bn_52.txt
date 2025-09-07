
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        out  = conv2d(x) 
        out = bn(out)
        return out


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 56, 56)
