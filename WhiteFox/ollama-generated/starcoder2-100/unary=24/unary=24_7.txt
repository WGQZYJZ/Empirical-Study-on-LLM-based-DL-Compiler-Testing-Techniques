
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25) -> None:
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 > 0).type(torch.FloatTensor)
        v3 = v1 * -self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model with negative slope value of 0.5
m = Model(negative_slope=0.75)

# Inputs to the model for initial and final versions (without and with changes in negative slope parameter values)
x = torch.randn(1, 3, 64, 64)
__output1__ = m(x) # output without changing negative_slope value
__output2__ = m(x) # output after changing the value of the negative_slope to 0.75

