
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, t2):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        return torch.where(t2, v1, v3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
t2 = torch.randn(1, 1) * 0.5
