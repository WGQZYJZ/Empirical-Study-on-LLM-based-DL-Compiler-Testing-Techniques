
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) 
        v4  = torch.clamp_max(v3, 6) 
        v5  = v4 / 6  
        return v5


# Initializing the model