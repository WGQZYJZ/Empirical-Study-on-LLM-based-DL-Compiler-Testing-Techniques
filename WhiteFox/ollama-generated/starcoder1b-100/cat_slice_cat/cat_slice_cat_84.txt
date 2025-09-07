
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1  = self.conv(x1)
        v2  = torch.cat([x1[:, 0:9223372036854775807], x2[:, 0:9223372036854775807]], dim=1)
        v3  = v1 * torch.cat([v1[:, 0:9223372036854775807], v2[:, 0:9223372036854775807]], dim=1)
        v4 = torch.erf(v3) + 1
        v5 = v4 * v2 * v3
        return v5


# Initializing the model
m = Model()


