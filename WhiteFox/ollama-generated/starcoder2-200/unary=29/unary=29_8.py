
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 16, 4)
    
    def forward(self, x1):
        v0 = self.deconv(x1)
        v5 = torch.clamp_min(v0, min=78.9)
        v6 = torch.clamp_max(v5, max=23.45) 
        return v6

# Initializing the model
m  = Model()

 # Inputs to the model 
 x1 = torch.randn(1, 3, 64, 64)
  __output__  = m(x1)
