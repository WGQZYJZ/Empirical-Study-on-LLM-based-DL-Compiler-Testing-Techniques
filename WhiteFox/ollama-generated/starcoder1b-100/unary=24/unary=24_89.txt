
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0., v1 * negative_slope, torch.zeros_like(v1))
        v3 = torch.mul(v2, -0.5, out=None)
        v4 = torch.relu(torch.erf(v3), inplace=True)
        v5 = torch.mul(v1, v4, out=None)
        return v5


# Initializing the model
m = Model(negative_slope=0.1)


