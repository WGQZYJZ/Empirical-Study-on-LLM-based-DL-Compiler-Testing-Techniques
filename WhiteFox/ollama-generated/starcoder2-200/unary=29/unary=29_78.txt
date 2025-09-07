

class Model(torch.nn.Module):
    def __init__(self, maxv=30):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 64, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2 = torch.clamp_min(v1, min=0.)
        v3 = torch.clamp_max(v2, max=500. if 5 else None, maxv) # Please note the keyword argument
        return v3
        
# Initializing the model