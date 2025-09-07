
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2, min=0) # Min value
        v4  = torch.clamp_max(v3, max=6) # Max value
        return v4 / 6


# Initializing the model
m  = Model()
__output__  = m(x1)
