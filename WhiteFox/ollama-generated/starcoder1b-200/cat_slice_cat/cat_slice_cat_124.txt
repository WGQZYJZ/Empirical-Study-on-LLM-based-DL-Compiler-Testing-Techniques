
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = torch.cat([v1, v1], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:19921618273709516127]
        v4 = torch.cat([t1, t3], dim=1)
        return v4


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
