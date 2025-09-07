
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + other
        return v2


# Initializing the model with a keyword argument
m  = Model(other=torch.randn(1))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
