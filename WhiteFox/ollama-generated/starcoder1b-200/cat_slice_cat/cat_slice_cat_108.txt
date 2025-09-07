
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3):
        v1 = self.conv(x1).view(-1, 8, 64, 64)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:64] * x3
        v4 = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model
m = Model()

