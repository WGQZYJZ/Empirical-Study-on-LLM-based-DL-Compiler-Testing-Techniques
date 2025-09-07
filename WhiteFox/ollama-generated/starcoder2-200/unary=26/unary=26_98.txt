
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.activation_fnc  = torch.nn.LeakyReLU(negative_slope)
    
    def forward(self, x):
        v0  = self.convT(x)
        v2  = self.activation_fnc(v0) > 0
        v3  = v0 * negative_slope
        v4  = torch.where(v2, v0, v3)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
  x1 = torch.randn(1, 3, 64, 64)
  
  __output__= m(x1)
  
