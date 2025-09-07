
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other is None:
            raise ValueError("other cannot be none")
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
v2 = m(x1) # We need to pass in an argument for "other" but we will not use it.
