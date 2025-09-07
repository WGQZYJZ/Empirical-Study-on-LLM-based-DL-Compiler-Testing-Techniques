
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1   = self.conv(x)
        v2   = v1 + 3
        v3   = torch.clamp_min(v2, 0)
        v4   = torch.clamp_max(v3, 6)
        v5   = v1 * v4 
        v6   = v5 / 6  
        return v6

# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
