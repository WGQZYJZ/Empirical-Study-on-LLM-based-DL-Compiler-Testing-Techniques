
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).type(torch.int32)
        v4  = torch.nn.functional.leaky_relu(v1, negative_slope=self.negative_slope)
        v5  = v4 * -self.negative_slope 
        v6  = torch.where(v2, v1, v5 )
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)