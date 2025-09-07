
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0., max_value=1.):
        v1 = self.conv(x1)
        v2 = torch.clamp(v1, min_value, max_value)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
min_value = 0.1
max_value = 5.0
x1 = torch.randn(1, 3, 64, 64)
