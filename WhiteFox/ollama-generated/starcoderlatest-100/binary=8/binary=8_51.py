
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v6


# Initializing the model
other = torch.randn(4, 8, 1, 1) # A different tensor than the previous one is passed to forward as an argument.
m = Model(other=other)

