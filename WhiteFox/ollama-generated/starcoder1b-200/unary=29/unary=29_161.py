
class Model(torch.nn.Module):
    def __init__(self, min_value=1.0e-3, max_value=1.0e+3):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 3, 1, stride=1, padding=1)
        self.clamp = torch.nn.Clamp(min_value, max_value)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.clamp(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
