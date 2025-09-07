
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = (v1 > 0).float() * (-self.negative_slope + v1)
        return torch.where(v2 == -self.negative_slope+v1, v1, v2)


# Initializing the model
m = Model(negative_slope=0.456789031925)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

