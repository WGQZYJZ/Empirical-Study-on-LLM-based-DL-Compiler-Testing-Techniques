
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3 
        v3 = torch.clamp(v2, min=0) # clamp(v2, min=0) -> torch.clamp(v2, 0, 6)
        v4 = torch.clamp(v3, max=6) # clamp(v3, max=6) -> torch.clamp(torch.clamp(v2, 0, 6), 6, 128) 
        v5 = v1 * v4 # multiply(v1, v4): [3, 7]
        v6 = v5 / 6 # divide(v5, 6) -> torch.div(v5, 6)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 28, 28)
