
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.m2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.m1(x)
        v2 = self.m2(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(8, 3, 3, 3)
