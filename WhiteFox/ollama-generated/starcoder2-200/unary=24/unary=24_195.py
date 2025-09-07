
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).float() * 0 - self.negative_slope + (torch.abs(v1).bool() * torch.ones_like(v1)) + 0.5
        return v2


# Initializing the model and setting the negative slope value
negative_slope = 3 # You can set this to a higher or lower number depending on your preference
m = Model(negative_slope)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__= m(x1)


