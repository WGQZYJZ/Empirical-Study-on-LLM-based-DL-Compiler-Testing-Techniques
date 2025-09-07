

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2 = torch.clamp_min(v1 + 3 ,0 )
        v4 = torch.clamp_max(v2 ,6) # clamp_max: [0,inf]
        v5 = v4 /6
        return v5

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

