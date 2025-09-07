
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 3).clamp_(0.,6.)
        v3 = torch.clamp(v2, 0.,6.)
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = v5 / 6
        return v6

 # Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
