
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
negative_slope  = 5.876e-09 # Any nonzero value other than negative infinity is a valid negative slope for this function
x1  = torch.randn(1, 3, 4, 4)


