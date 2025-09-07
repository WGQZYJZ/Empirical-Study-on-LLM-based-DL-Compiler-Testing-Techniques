
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn = torch.nn.BatchNormXd(...)
        self.output = self.bn(self.conv(input_tensor))

    def forward(self, x1):
        return self.output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
