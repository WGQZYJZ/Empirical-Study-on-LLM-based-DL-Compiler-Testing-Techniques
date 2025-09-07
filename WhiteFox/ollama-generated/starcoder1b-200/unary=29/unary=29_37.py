
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, min_value=None, max_value=None):
        v1 = self.conv(x1)
        v2 = v1.clamp(min_value=min_value).clamp(max_value=max_value)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
