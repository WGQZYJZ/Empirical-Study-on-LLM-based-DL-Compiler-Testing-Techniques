
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        if not other is None:
            self.other = other
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + self.other
        return v2


# Initializing the model with the second parameter as keyword argument
m = Model(torch.randn(3))


# Inputs to the model (other is passed in as a keyword argument here)
x  = torch.randn(1, 3, 64, 64)
__output__  = m(x, other=None)

