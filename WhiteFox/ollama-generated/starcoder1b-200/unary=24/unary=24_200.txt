
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # This operation creates a boolean mask where each element is True if the corresponding element in t1 is greater than 0
        v2 = torch.where(v1 > 0, v1, - self.negative_slope * v1)
        return v2


# Initializing the model
m = Model()
m.negative_slope = -0.75
x1 = torch.randn(1, 3, 64, 64)
