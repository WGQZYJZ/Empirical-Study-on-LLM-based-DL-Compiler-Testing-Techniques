
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other_tensor
        return v1

# Initializing the model with an "other" tensor as its keyword argument (equivalent to setting `m = Model()` in earlier models).
o = torch.randn(1, 8, 64, 64)
m = Model(other_tensor=o)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
