
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 7, stride=2, padding=3)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = self.conv1(x2)
        v3 = self.conv1(x3)
        v4 = self.conv1(x4)
 
        v5 = torch.mm(v1, v2) # Matrix multiplication between two 64 x 3 x 64 x 64 results of the first convolution layer
        v6 = torch.mm(v3, v4) # Matrix multiplication between two 64 x 3 x 64 x 64 results of the second convolution layer
        v7 = v5 + v6 # Addition of the two matrix multiplications
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 16, 16)
x3 = torch.randn(2, 3, 8, 8)
x4 = torch.randn(2, 3, 4, 4)
