
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(32, 16, 3, stride=2)
        self.act = torch.nn.LeakyReLU()
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = (v1 > 0).float().view(-1, 32) * (-0.5)
        v3 = torch.where(v2 == True, v1, v2)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(16, 32, 48, 90)
  __output__  = m(x1)
 
