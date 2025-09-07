

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v0 = torch.randn(256)  # Create random vector of length 256
        v1 = self.conv(x1)  # Apply pointwise convolution with kernel size 3 to the input tensor. The resulting tensor will be of shape (N, M, 32, 32). Where N is the number of data points processed by the forward pass; and M is the total number of channels in this particular layer/convolution
        v0 = torch.cat([v0] * x1.shape[0])  # Create a tensor with shape (N, ) where each element is equal to `v0`
        v2 = v1 + v0 
        v3 = torch.clamp(v2, -500.0) 
        v4 = v3 / 6.0 
        return v4 


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8, 3, 32, 32)
__output__  = m(x1)
