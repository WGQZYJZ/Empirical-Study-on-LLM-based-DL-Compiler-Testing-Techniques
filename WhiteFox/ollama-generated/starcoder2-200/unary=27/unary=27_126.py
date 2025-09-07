
class Model(torch.nn.Module):
    def __init__(self, min_value=-10000, max_value=10000):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - 10000
        v3  = v2 + 10000
        return v3


# Initializing the model
m = Model()
__output__  = m(torch.randn(1, 3, 64, 64))

