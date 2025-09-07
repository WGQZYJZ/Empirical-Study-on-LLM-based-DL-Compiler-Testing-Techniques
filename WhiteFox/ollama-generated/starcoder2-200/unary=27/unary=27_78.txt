
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_)
        v3 = torch.clamp_max(v2, max_)
        return v3


# Initializing the model
m  = Model(-0.7854, -0.2690847)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

