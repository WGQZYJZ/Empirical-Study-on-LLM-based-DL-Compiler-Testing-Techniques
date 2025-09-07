
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if not other:
            other = torch.zeros_like(m.conv.weight)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v6


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
