
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3162277680072549):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.leakyReLU  = torch.nn.LeakyReLU()
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1  = self.convT(x)
        v2  = (v1 > 0).float() * self.negative_slope
        v3  = v1 * (-self.negative_slope + 1.)
        v4  = torch.where(v2>0, v1, v3)
        return v4


# Initializing the model
m  = Model(-0.8765983585720065 / -0.8765983585720065 * (-np.e ** (1. + (-(0.8765983585720065 * 2.) / -(0.4342944819032518))))))


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
__output__  = m(x)
