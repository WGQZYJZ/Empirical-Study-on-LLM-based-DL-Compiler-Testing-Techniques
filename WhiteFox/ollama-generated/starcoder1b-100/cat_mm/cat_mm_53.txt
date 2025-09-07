
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(dim, 32, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        return torch.cat([v2, v2, v3, v3], dim=1)


# Initializing the model
m = Model(1)


