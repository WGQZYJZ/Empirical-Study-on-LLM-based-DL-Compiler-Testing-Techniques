
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if (other is not None):
            v2 = v1 + other
        else:
            v2 = v1 + torch.randn_like(v1)
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
