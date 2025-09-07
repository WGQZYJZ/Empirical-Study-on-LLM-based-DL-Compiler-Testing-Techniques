
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        v3 = torch.mm(v1, v2) # Matrix multiplication between input1 and input2
        v4 = torch.mm(v3, x3) # Matrix multiplication between the result of previous matrix multiplication and input3
        v5  = v3 + v4
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
x3 = torch.randn(8, 8)
x4 = torch.randn(8, 8)
