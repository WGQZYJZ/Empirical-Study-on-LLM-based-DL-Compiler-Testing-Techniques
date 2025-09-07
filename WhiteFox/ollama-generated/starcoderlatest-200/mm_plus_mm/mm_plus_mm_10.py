
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64) # Input of the first matrix multiplication
x2 = torch.randn(1, 8, 64, 64) # Input of the second matrix multiplication
x3 = torch.randn(1, 3, 64, 64) # Input of the third matrix multiplication
x4 = torch.randn(1, 3, 64, 64) # Input of the fourth matrix multiplication
