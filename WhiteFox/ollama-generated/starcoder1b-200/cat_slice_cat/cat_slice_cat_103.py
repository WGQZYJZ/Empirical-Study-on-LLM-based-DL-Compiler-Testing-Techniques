
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
 
    def forward(self, x1, x2):
        c1 = self.conv1(x1)
        c2 = self.conv2(c1)
        v = torch.cat([c1, c2], dim=1)
        return v


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
