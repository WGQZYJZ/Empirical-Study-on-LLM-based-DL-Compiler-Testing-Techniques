
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = v1 > 0
        v2 = v1 * -0.5
        v4 = torch.where(t1, v1, v2)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
