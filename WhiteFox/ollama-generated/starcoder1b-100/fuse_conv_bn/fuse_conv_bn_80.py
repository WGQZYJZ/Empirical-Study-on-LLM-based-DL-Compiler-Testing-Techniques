
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...)

    def forward(self, x):
        conv = self.conv(x)
        bn   = self.bn(conv)
        output = bn(conv)
        return output


# Inputs to the model
x1 = torch.randn(1, 2, 2)
