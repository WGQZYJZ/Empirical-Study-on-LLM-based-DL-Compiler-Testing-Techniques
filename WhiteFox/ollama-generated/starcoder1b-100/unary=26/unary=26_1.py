
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 3)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = v1 * self.negative_slope
        v3 = torch.where(v1, x1, -torch.log(1 - self.negative_slope))
        return v2


# Initializing the model
m = Model()


