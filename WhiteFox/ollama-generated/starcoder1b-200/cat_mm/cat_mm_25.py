
class Model(torch.nn.Module):
    def __init__(self, dim=128):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 64, 3, stride=2, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.cat([v1, v1, ..., v1], dim=dim) # Concatenation of the result tensor along a specified dimension
        return v2


# Inputs to the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
