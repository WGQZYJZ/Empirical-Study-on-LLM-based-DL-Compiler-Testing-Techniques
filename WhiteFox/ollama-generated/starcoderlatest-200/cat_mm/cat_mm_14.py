
class Model(torch.nn.Module):
    def __init__(self, shape1, shape2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.cat([v1, v1])
        return v2


# Initializing the model
m = Model(shape1=[8, 4], shape2=[16, 4])

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
