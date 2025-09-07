
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + other_tensor


# Initializing the model with a random tensor as "other" input
m = Model(torch.rand(32, 8, 64, 64))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
