
class Model(torch.nn.Module):
    def __init__(self, use_conv=False):
        super().__init__()
        self.use_conv = use_conv
        if use_conv:
            self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=(3, 3))
            self.bn1 = torch.nn.BatchNorm2d(64)
            self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        else:
            self.conv = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
            self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x):
        if self.use_conv:
            out = self.conv1(x)
            out = self.bn1(out)
            out = self.pool(out)
        else:
            out = self.conv(x)
            out = self.bn(out)
        return out


# Initializing the model
m = Model(use_conv=True)

# Inputs to the model
x1 = torch.randn(2, 3, 50, 50)
