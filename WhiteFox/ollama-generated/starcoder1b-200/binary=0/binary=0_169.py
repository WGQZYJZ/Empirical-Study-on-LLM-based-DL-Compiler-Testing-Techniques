
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, y):
        v1 = self.conv(x1)
        return v1 + y


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
y  = torch.randn(1, 3, 64, 64)
