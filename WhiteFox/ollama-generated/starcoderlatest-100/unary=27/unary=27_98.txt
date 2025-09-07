
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp(v1, min=self.min_value, max=self.max_value)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
