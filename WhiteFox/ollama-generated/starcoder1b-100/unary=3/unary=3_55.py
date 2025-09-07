
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.conv2d(x1, 0.5)
        v2 = F.conv2d(v1, 0.7071067811865476)
        v3 = torch.erf(v2) + 1
        v4 = F.conv2d(v3, 1.0) * v2
        return v4


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
