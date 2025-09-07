
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other is not None:
            self._register_buffer('other', other)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self['other'] 
        return v2


# Initializing the model with a new tensor as keyword argument to the addition operation.
t  = torch.randn(3)
m = Model(other=t)


# Inputs to the model (after passing in this new tensor t to the model).
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)['other']