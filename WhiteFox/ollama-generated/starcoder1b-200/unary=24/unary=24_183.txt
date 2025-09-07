
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * (1 - negative_slope)
        v3 = v2 * (1 + negative_slope)
        return v3


# Initializing the model
m = Model()
negative_slope = 0.5
