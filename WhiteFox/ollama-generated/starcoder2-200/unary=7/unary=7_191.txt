
class Model(torch.nn.Module):
    def __init__(self, m1, m2):
        super().__init__()
        self.conv = torch.nn.Conv2d(m1 * m2 + 3, 8)
 
    def forward(self, x1):
        l1 = self.conv(x1)
        l2 = l1 * clamp(min=0, max=6, l1 + 3) / 6
        return l2


# Initializing the model
m = Model(45, 78)


# Inputs to the model
x1 = torch.randn(1, m, 90, 90)
