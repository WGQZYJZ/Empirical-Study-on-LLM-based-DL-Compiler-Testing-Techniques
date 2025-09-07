
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = torch.nn.Parameter(torch.tensor(-0.1))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0
        negative_slope = -0.1
        v2 = v1 * negative_slope
        v3 = torch.where(mask, v1, v2)
        return v3


# Initializing the model and setting the initial values of all the parameters
m = Model()
m.negative_slope.data.fill_(-0.1)
