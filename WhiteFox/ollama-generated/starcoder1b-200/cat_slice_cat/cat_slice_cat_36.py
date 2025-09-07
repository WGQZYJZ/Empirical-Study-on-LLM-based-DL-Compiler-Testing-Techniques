
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([x1, v1], dim=1)
        v3 = v2[:, 0:size]
        v4 = torch.cat([v2, v3], dim=1)
        return v4


# Initializing the model
m = Model()


