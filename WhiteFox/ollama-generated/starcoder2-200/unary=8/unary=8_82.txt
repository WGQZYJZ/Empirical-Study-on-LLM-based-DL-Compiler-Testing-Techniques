
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + 3
        v3 = F.clamp(v2, min=0) 
        v4 = F.clamp(v3, max=6)   
        v5 = v1 * v4      
        return v5 / 6

# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(1, 8, 256, 256)
__output__  = m(x)

