
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(in_features=8 * 5 * 5, out_features=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1, negative_slope * v1)
        v3 = v1 * positive_slope
        v4 = torch.where(v2, v3, negative_slope * v3)
        return v4


# Initializing the model
m = Model()


