
class Model(torch.nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)
        self.bn    = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1 = self.conv(x1)
        bn = self.bn(v1)
        return bn


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
