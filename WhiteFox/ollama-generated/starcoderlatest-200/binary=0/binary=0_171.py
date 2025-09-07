
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other is not None:
            v2 = v1 + other
        else:
            raise ValueError('Other tensor must be passed as keyword argument.')
        return v6

# Initializing the model with an input to the model and additional inputs to add 
m = Model(torch.randn(1, 3, 64, 64))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
