
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 4, stride=2, padding=1) # Note that the stride parameter is set to a value of two in this layer.
        self.conv2 = torch.nn.Conv2d(8, 16, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.tanh(v1) # Apply the hyperbolic tangent function to the output of the pointwise convolution layer with a kernel size of 4 and stride of 2 and padding of 1
        v3 = self.conv2(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
