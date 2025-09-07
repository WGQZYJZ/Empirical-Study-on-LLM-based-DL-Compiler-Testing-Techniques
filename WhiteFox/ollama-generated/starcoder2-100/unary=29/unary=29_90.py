
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min(-0.5)) 
        v3  = torch.clamp_max(v2, max(0.5)) 
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 8, 74 + 96, 74 + 96)
__output__  = m(x1)
 
