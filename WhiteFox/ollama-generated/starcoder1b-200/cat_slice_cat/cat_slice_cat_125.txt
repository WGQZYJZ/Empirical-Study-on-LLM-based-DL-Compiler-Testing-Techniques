
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.cat([v1[:, 0:9223372036854775807], x2], dim=1)
        return torch.cat([x1, v2], dim=1)


# Initializing the model
m = Model()

