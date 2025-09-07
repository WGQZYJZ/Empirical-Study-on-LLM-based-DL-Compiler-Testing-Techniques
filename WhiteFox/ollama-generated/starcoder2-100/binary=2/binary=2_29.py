
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor | float = None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self._other  = other
 
    @property
    def other(self):
        return self._other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3,8,64,64)
m.other  = x1  # This line will update the parameter 'other' in m object
__output__  = m(x1)

