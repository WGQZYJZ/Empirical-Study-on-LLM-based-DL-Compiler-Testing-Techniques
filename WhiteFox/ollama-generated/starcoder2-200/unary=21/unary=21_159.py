
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.tanh(v1) # Apply the hyperbolic tangent function to the output of the convolution
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
__output__  = m(x1) # This is the output from PyTorch

# Inputs to the model
x2 = torch.randn(3, 9, 50, 77) # Input with different size

