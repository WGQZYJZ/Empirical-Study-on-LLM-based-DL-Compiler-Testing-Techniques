
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2,0) # Clamped to minimum of 0.
        v4 = torch.clamp_max(v3,6)  # Clamped to maximum of 6.
        v5 = v4 / 6             # Divided by 6.
        return v5

# Initializing the model
m = Model()


x1 = torch.randn(1,3,64,64)
