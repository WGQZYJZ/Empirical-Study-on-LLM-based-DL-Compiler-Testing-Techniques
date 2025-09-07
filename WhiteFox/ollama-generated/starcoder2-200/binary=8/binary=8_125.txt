
class Model(torch.nn.Module):
    def __init__(self, m):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self._m  = m
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self._m
        return v2


# Initializing the model
m  = Model(m=m)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) # Same as previous example!
__output__  = m(x1)

