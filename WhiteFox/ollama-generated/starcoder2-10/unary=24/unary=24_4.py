
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.leakyrelu  = torch.nn.LeakyReLU()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0 
        v3  = -0.4
        v4  = torch.where(v2, v1, v3) # replace all negative values in v with negative_slope
        return self.leakyrelu(v4)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
