
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1 + other

# Initializing the model with a random tensor for the argument of the `other` keyword to be added in the model's `__init__` method.
m_ = Model(torch.randn(3, 8))

