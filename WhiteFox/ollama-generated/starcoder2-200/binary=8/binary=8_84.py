
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.other = other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1 + self.other


# Initializing the model with some initial tensor as keyword argument "other" of type FloatTensor
m = Model(torch.randn(40))


# Inputs to the model
x2 = torch.randn(3, 8, 64, 64)
__output__  = m(x2)

