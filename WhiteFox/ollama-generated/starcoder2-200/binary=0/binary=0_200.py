
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Pointwise convolution with kernel size 1 to the input tensor
        return v1


# Initializing and passing inputs as keyword arguments
x1 = torch.randn(1,3,64,64)
other = torch.randn(10,8,27,93)
m  = Model()
