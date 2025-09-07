
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = torch.full([v1.size()[0], v1.size()[1]], 5378, dtype=torch.float32) # Create a tensor filled with the scalar value 5378 with the specified dtype and size as that of `v1`
        v4  = self.conv(x1).clone() # Clone the result from `self.conv()` with the same shape and device, and pin memory
        v6  = torch.cumsum(torch.zeros([20], dtype=torch.float32), 1) # Create a tensor filled with the scalar value 0 with the specified size
        return v4 + v6

# Initializing model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 9, 8)
__output__  = m(x1)

