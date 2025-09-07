
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv(x1)  # Apply a pointwise convolution to the input tensor `v3`
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 56, 56)
other = 0.8 * 0.7 # Generate a random number of the same data type as `v3`
__output__  = m(x1), other

