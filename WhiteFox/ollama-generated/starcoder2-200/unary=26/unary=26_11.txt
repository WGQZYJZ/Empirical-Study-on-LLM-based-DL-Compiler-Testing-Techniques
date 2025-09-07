
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).type(torch.float) 
        v3  = v1 * (-1) * v2 + v1 #v2
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

