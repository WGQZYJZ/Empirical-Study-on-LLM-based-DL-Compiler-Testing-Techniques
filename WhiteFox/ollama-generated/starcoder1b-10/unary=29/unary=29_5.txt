
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v  = self.conv(x)
        m  = v * torch.ones_like(v)
        return m - torch.zeros_like(m).clamp(min=0.5)

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
