
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other
        return v2


# Initializing the model
m0  = Model(other=torch.zeros([1]))
m   = Model(other=other) # Different from m0!

# Inputs to the models
x1  = torch.randn(3, 64, 64)
__output__1__ = m0(x1), m(x1)

