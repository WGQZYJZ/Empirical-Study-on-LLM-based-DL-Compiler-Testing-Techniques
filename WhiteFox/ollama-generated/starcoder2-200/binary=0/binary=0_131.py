
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + other
        return v2


# Initializing the model with another tensor to be added in the output of a pointwise convolution (here: the zero vector). The same code works for a single-layer convolution!
other_tensor  = torch.zeros(3,8,64,64) # Other tensor to add at the output of the convolutional layer. Note that the dimensions should match those of the convolution kernel (in this case: [3,8] for 5x5 kernels and [1,32])
m = Model(other_tensor)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
