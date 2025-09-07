
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(2, 1, kernel_size=3, stride=1, padding=0)
        self.bn = torch.nn.BatchNormXd(1)

    def forward(self, x):
        output = self.bn(self.conv(x))
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 3, 3)
