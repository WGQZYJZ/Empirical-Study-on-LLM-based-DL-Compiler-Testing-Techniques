
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.375):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 16, 3, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        mask = v1 > 0
        v2  = v1 * negative_slope
        v3  = torch.where(mask, v1, v2)
 
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
 
# Evaluating the model
__output__= m(x1)
