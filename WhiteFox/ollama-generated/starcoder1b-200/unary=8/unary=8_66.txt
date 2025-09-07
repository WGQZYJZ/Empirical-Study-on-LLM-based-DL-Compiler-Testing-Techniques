
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 10, 3, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        v2 = v1.clamp_(min=0).clamp_(max=6)
        v3 = v2 * v4 / 6
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
