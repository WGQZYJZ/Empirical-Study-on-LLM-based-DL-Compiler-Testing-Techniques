
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1e-3):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = F.leaky_relu(self.conv(x1))
        v2 = v1 * self.negative_slope
        v3 = v1  * self.negative_slope
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2  * v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
