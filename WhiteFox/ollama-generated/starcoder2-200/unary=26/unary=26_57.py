
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1)
        self.leakyReLu = torch.nn.LeakyReLU()
 
    def forward(self, x):
        v1 = self.convT(x)
        v2 = (v1 > 0).float() * negative_slope + v1.sigmoid() - negative_slope
        return v2


# Initializing the model
m = Model(-0.3576994484317769)
 
 # Inputs to the model 
 x = torch.randn(1, 8, 32, 32)
 
 __output__  = m(x)
 
