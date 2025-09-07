

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0) # Clamped 6
        v4 = torch.clamp_max(v3, 6) # Clamped max value of 8
        v5 = v4 / 7  # Divided by 10, as the max output was increased by another ten units (10, 20 ...)
        return v5

# Initializing model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 8, 64, 64) # Input with different shape and size
__output__  = m(x1)
 


