
class Model(torch.nn.Module):
    def __init__(self, t2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.t2 = t2
 
    def forward(self, x1):
        v1 = self.conv(x1) + self.t2
        return v1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
t2 = torch.randn(1, 1, 1, 8)
