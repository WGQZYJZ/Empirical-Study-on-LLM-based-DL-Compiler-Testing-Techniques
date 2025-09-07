
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, y):
        v1 = self.conv(x1)
        return v1 + y


# Initializing the model
m = Model(torch.randn(10))


# Inputs to the model
x1  = torch.randn(3, 1, 28, 28)
y   = torch.randn(5, 4, 6, 6)
