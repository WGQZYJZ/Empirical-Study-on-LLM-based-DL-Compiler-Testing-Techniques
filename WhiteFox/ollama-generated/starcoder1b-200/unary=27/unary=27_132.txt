
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0, max_value=None):
        v1 = self.conv(x1)
        if max_value is not None:
            v2 = torch.clamp_max(v1, max_value)
        else:
            v2 = v1 * 0.5
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
