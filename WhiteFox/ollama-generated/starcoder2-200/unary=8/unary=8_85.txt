
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = F.clamp(v2, min=0) 
        v4  = F.clamp(v3, max=6)
        v5  = v1 * v4
        v6  = v5 / 6
        return v6

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(20, 3, 64, 64)

# Outputs from the model
