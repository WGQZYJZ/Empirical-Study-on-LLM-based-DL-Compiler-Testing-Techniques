
class Model(torch.nn.Module):
    def __init__(self, somearg):
        super().__init__()
        self.somearg = somearg
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
 
        return v1 + self.somearg

# Initializing the model with argument "somearg" set to a constant value.
m  = Model("some_constant")

# Inputs to the model with an additional input that gets added on top of convolution output.
x1  = torch.randn(1, 3, 64, 64)
x2  = x1 + 1 # Some constant
__output__  = m(x1, x2)

