
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        mask = (x1 > 0).float()
        v = mask * self.negative_slope
        y = self.conv(x1)
        return v * y


# Initializing the model
m = Model()

