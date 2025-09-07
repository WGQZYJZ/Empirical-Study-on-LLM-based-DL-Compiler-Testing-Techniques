
class Model(torch.nn.Module):
    def __init__(self, x2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self._x2 = x2
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self._x2 
        return v2


# Initializing the model and specifying other tensor as the addition operation
other  = torch.randn(4, 3, 64, 64)
m  = Model(other)
# Inputs to the model
__x1  = torch.randn(1, 3, 64, 64)

__output__  = m(__x1)

