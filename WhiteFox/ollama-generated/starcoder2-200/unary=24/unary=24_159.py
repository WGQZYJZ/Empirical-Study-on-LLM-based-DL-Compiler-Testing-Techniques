
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t0 = torch.zeros(*v1.shape)
        v2 = torch.where(v1 > 0, v1, t0 + self.negative_slope * (v1 - 0))
        return v2


# Initializing the model
m = Model(0.5)
 
# Inputs to the model
x1 = torch.randn(3, 8, 4, 4)
__output__  = m(x1)

