
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v0 = x1 # Save the input tensor
        v1  = self.conv(v0) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = torch.nn.ReLU()(v1 - v1[-1]) # Subtract a tensor or scalar "other" from the output of the convolution, then apply the ReLU (Rectified Linear Unit) activation function to the result
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__  = m(x1)