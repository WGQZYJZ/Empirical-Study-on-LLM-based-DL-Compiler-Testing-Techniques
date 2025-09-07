
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1  = self.conv(x)
        v4  = 3 + v1
        v5  = torch.clamp_min(v4, 0)
        v6  = torch.clamp_max(v5, 6)
        return v6 / 6


# Initializing the model
m  = Model()
 
# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
__output__   = m(x)

