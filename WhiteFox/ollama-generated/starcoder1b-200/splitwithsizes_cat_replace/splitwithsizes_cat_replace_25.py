
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, y2):
        v1 = self.conv(x1)
        v2 = torch.split(v1, 2, dim=-1)
        v3 = [v2[0] * 0.5 for v2 in v2]
        v4 = [torch.erf(x2) for x2 in v3]
        return v4


# Initializing the model
m = Model()


