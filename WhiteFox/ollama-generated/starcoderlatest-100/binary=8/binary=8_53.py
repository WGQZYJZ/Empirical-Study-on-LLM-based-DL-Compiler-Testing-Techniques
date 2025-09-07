
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other is None:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1, bias=False)
        if other is None:
            self.bias = torch.nn.Parameter(torch.zeros(1))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
m.other = torch.nn.Parameter(torch.ones(1))
