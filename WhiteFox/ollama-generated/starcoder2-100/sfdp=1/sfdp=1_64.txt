
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.norm = torch.nn.GroupNorm(4, 8)
 
    def forward(self, x0):
      v0  = self.conv(x0)
      v0 = self.norm(v0)
      return v0

m  = Model()

 # Inputs to the model
 x1  = torch.randn(32, 3, 64, 64)
__output__  = m(x1)