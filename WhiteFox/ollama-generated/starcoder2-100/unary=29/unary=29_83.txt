
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        return torch.clamp_min(v1, min=0.), torch.clamp_max(v1, max=5.)

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
  __output__  = m(x1)

