
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3):
        v1  = self.conv(x1)
        v2 = v1  * 0.5
        v3 = t1[:, 0:9223372036854775807]
        v4 = torch.cat([t1, t3], dim=1)
        return v4


# Initializing the model
m = Model()


