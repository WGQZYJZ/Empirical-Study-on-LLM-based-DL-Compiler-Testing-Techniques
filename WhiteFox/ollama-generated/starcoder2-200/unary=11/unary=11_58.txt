
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + 3
        v3  = F.clamp_min(v2, min=0)
        v4  = torch.clamp(v3, max=6)
        v5  = torch.div(v4, divisor=6, rounding_mode="floor")
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(20, 8, 32, 32)
__output__  = m(x1)
