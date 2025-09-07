 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)

    def forward(self, x1):
        bn = torch.nn.BatchNormXd(...)
        y  = self.conv(x1)
        z  = bn(y)
        return z


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 3)
