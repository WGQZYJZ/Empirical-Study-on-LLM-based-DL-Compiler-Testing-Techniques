
class Module(torch._C.nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.conv  = torch._C.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch._C.nn.BatchNormXd(...)

    def forward(self, x):
        v = self.conv(x)
        return self.bn(v)


# Initializing the model
m = Module()


