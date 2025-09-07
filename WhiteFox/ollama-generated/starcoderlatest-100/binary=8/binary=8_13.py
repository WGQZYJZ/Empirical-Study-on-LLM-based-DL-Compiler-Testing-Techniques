
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other
        return v6


# Initializing the model and adding a constant "other" to an input tensor x1:
m = Model()
x2 = torch.randn(1, 3, 64, 64)
