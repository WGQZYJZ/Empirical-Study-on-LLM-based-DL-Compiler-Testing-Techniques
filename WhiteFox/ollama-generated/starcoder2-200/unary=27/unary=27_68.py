
class Model(torch.nn.Module):
    def __init__(self, min=100, max=200):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min_value)
        v4  = torch.clamp_max(v3, max_value)
        return v6


# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

