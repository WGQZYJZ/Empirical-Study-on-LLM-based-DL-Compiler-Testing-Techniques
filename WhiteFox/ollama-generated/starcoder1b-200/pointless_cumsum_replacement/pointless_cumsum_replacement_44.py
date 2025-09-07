
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(-1, 8, -1, 1)
        v2 = (v1 ** 0.5).sum(dim=(2,3), keepdims=True)
        return torch.cumsum(v2, dim=1)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)
