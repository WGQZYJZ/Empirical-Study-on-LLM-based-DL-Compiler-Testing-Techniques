
class Model(torch.nn.Module):
    def __init__(self, some=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2 = v1 + some # <-- The "some" argument is passed as keyword argument to the addition operation
        return v2


# Initializing the model
some_value = 0.5637489295426474  # A random value
m  = Model(some=some_value)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

