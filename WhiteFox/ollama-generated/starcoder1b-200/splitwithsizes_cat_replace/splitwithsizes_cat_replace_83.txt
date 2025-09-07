
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1, x2)
        v2 = torch.split(v1, (2,), dim=0)
        v3 = torch.cat([torch.mul(v, 0.5) for v in v2], dim=0)
        v4 = torch.mul(torch.erf(v3), 1.0) + 1
        v5 = torch.mul(v4, torch.mul(v2, 0.7071))
        return v5


# Initializing the model
m = Model()


