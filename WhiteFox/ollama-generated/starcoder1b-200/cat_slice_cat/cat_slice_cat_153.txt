
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = x1[:, 0:9223372036854775807]
        v2 = t1[:, 0:size]
        v3 = torch.cat([v1, v2], dim=1)
        return v3


# Initializing the model
m = Model()


