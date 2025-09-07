
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 > 0
        v4  = v1 * negative_slope
        v5  = torch.where(v2, v1, v4)
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(3, 8, 64, 64)
  __output__  = m(x1)

