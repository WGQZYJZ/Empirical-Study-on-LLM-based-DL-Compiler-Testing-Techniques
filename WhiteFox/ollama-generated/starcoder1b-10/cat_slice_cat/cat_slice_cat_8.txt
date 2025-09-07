
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv(x1)
        v2 = t2 * t3[:, :, 0:size]
        v3 = self.conv(t4)
        return torch.cat([v1, v2], dim=1)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 9223372036854775807, 1)
x3 = x1[:, 0:9223372036854775807]
x4 = x1 * x2 + x3 + torch.randn(1, size, size, 1)


# Outputs of the model
