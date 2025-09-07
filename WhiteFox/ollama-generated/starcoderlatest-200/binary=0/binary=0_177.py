
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other == None:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1, bias=True)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + other


# Initializing the model
m = Model(torch.randn(1, 3, 64, 64))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
