
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=0.) # clamped to a minimum value of 0
        return torch.clamp_max(v2, max=5.)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
