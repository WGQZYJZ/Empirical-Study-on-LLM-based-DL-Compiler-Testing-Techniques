
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.ConvTranspose2d(3, 8, 4)
 
    def forward(self, x1):
        v1 = self.conv1(x1) + 3 
        v2 = F.clamp(v1, min=0)
        v3 = F.clamp(v2, max=6)
        v4 = v1 * v3
        v5 = v4 / 6.0
        return v5

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 96, 72) # Note that x1 is different from x1 in previous example!
__output__  = m(x1)

