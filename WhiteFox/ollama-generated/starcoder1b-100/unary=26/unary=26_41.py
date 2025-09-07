
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.01):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 3)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = F.leaky_relu(self.conv(x1), self.negative_slope)
        return v1

# Initializing the model
m = Model()
__output__  = m(torch.randn(1, 3, 64, 64))

