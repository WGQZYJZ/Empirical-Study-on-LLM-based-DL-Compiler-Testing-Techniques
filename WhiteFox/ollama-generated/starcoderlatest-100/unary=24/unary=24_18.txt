
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float=0.01):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t2 = (v1 > 0).float()
        t3 = t1 * self.negative_slope
        t4 = torch.where(t2, t1, t3)
        return t4


# Initializing the model
m = Model(negative_slope=0.005)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
