
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 5, stride=4)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).type_as(v1) * -1. + (v1 < 0).type_as(v1) * negative_slope
        v3  = torch.where(v2, v1, v2)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(5, 8, 640, 750)
 
 __output__  = m(x1)
