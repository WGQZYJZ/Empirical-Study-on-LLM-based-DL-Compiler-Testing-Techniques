
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = F.clamp(v2, min=0) # clamp(v3, max=6) 
        
        return torch.div(torch.mul(v3, v1), 6).detach()


# Initializing the model
m = Model()
 
 
