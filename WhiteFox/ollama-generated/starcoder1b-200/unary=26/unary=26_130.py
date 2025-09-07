
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        mask = torch.greater(x, 0)
        out = self.conv(x) * negative_slope
        out = torch.where(mask, out, -out)
        return out


# Initializing the model
m = Model(negative_slope=0.2)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
