
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return (v1 + other).clamp(min=-10, max=10)

# Initializing the model
m = Model()
# Inputs to the model
other_tensor = torch.randn(8,)
