
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4):
        v1 = self.conv(x1)
        v2 = self.split([v1, x2, x3], [5, 3])
        v3 = torch.cat(v2, dim=0)
        v4 = torch.cat([v2[1], v1], dim=1) * v4
        return v3

# Initializing the model
m = Model()


