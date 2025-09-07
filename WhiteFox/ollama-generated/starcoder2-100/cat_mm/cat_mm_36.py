
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=7)
        self.conv2 = torch.nn.Conv2d(8, 4, kernel_size=7)
 
    def forward(self, x0):
        v1 = self.conv1(x0) # Apply pointwise convolution with the kernel size of 7 to an input tensor
        v2 = self.conv2(v1) # Apply pointwise convolution with the kernel size of 7 to the output of a pointwise convolution operation 
        v3 = torch.cat([v2, ...], dim=0) # Concatenate along dimension 0, the output of a pointwise convolution operation along the resulting dimension after concatenation will be [4 x 1]
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x0  = torch.randn(1, 8, 65, 7)
__output__  = m(x0)

