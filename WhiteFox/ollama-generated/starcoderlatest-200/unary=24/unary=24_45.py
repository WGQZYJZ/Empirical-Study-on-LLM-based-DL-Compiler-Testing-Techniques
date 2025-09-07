
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        self._negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0
        t1 = v1 * self._negative_slope
        t2 = torch.where(mask, t1, v1)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
