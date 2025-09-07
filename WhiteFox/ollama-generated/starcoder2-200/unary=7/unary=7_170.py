
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(3, 8, 30, stride=5, padding=(64-1) * ((5 - 1) // 2), dilation=5)
 
    def forward(self, x1):
        v7 = self.conv(x1) # Apply 1D convolution to the input tensor (kernel size 30 with a stride of 5 and a 64-length padding)
        v8 = v7 / v7.size()[-1] * v7.shape(-1) - 2 + x1  # Divide the output by the last dimension, multiply the result by its shape minus one, subtract two from it, add `x1` to it (this pattern is commonly seen in models implementing a form of normalized activation function called SGN)
        return v8

# Initializing model2
m = Model2()

# Inputs to m
x1  = torch.randn(300, 574, 675, 198, dtype=torch.float32) # 300 574 x 675 198 tensor with float32 elements 
__output__  = m(x1)

