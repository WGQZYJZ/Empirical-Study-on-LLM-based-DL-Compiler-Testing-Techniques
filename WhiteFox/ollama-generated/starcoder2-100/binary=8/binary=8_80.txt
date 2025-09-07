
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2


# Initializing the model and passing "other" tensor to the model constructor
m = Model(torch.randn(3))


# Inputs to the model with "other" passed as a keyword argument during the model initialization
x1  = torch.randn(1, 3, 64, 64)
