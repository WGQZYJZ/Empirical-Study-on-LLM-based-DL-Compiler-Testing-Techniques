
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1) # Number of input channels is 3 and number of output channels is 8, kernel size is 1, stride is 1, and padding is 1
        self.conv2 = torch.nn.Conv2d(8, 4, 1) # The convolution of a matrix with itself, which has the same effect as multiplying mat1 and mat2
    def forward(self, x):
        v1 = torch.addmm(x, x.view(x.size(0), -1).t(), x)
        v2 = torch.cat([v1], dim=1)
        v3 = self.conv2(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
