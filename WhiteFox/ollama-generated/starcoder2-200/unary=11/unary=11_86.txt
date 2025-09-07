
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(32, 8, 1)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2, 0) # min 0
        v4  = torch.clamp_max(v3, 6) # max 6
        v5  = v4 / 6  
        return v5


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(20, 8, 32, 32)
