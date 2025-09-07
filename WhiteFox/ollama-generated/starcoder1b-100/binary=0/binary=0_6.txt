
class Model(torch.nn.Module):
    def __init__(self, x1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1, *args, **kwargs):
        return self.conv(x1) + self.other(*args, **kwargs)


# Initializing the model
m = Model(x1)

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
