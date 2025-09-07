
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 4, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * x2
        return v2


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 4, 64, 64)
