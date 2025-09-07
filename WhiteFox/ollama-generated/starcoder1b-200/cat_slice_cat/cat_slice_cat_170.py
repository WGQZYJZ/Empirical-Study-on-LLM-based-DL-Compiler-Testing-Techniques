
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = t1[:,0:9223372036854775807]
        v3 = t2[0:size, :]
        v4 = torch.cat([v1, v3], dim=1)
        return v4


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 8, 64, 64)
