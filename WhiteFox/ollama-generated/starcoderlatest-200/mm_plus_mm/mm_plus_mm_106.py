
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.conv2 = torch.nn.Conv2d(8, 16, kernel_size=3)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
 
        v3 = torch.mm(v2, x3) + torch.mm(v2, x4) # Add the results of two separate matrix multiplications between convolution outputs and input tensors
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(8, 3, 16, 16)
x3 = torch.randn(16, 8, 8, 8)
x4 = torch.randn(8, 16, 8, 8)
