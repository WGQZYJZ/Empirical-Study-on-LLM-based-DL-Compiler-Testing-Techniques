
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        output = self.bn(self.conv(x1))
        return output
# Inputs to the model
x1 = torch.randn(1, 2, 2)
