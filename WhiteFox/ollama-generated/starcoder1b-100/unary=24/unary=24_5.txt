
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        mask = torch.logical_not(x > 0)
        out = F.leaky_relu_(self.conv(x * mask))
        return out


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
