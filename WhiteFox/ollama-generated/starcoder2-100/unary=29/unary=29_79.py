
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = torch.clamp_min(v1, min=0)
        v3  = torch.clamp_max(v2, max=10)
        return v3


# Initializing the model