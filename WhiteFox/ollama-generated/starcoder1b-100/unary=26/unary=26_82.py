
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv(x) * negative_slope
        return v


# Inputs to the model
negative_slope = 0.5
