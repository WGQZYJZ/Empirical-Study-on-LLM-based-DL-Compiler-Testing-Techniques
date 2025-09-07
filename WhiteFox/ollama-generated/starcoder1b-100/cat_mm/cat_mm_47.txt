
class Model(torch.nn.Module):
    def __init__(self, dim=1024):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        return torch.cat([v1, v1, ..., v1], dim)


# Inputs to the model
x1 = torch.randn(3, 64, 64, 8)
x2 = torch.randn(5, 1024, 1024, 8)
