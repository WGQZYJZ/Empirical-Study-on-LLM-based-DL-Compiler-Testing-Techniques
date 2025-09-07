
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(3, 2, kernel_size=3)
        self.bn = torch.nn.BatchNormXd(2)

    def forward(self, x1):
        output = self.conv(x1)
        bn_output = self.bn(output)

        return bn_output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 28, 28)
