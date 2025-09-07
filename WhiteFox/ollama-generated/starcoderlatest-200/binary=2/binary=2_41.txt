
class Model(torch.nn.Module):
    def __init__(self, other_t: torch.Tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other_t
        return v2


# Initializing the model
m = Model() # The constructor of Model will be called with no input tensor as its argument.

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
