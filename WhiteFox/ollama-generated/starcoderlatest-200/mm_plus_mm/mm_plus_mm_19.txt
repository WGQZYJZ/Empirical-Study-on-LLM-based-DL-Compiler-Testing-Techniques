
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv(x1)
        v2 = torch.mm(v1, v1.transpose(1, 2))
        v3 = torch.mm(x3, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 32, 32)
x3 = torch.randn(1, 16, 16, 16)
x4 = torch.randn(1, 16, 16, 16)
