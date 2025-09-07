
class Model(torch.nn.Module):
    def __init__(self, k1=32, k2=48):
        super().__init__()
        self.conv  = torch.nn.Conv2d(in_channels=k1, out_channels=k2, kernel_size=7)
 
    def forward(self, x0):
        v1 = self.conv(x0)
        v2 = torch.cat([v1] * k2, 3) # the number of times that tensor is concatenated along a dimension depends on k2
        return v2

# Initializing model parameters. If you specify the input shape in the forward() function, 
# it will be used as an initial parameter value, which ensures that all modules have the same parameter values at the beginning and throughout training.  
# Otherwise, the module parameters are initialized randomly. 
# For example, here we define the first convolutional layer of the model `m1` to have three input channels, eight output channels (i.e., the parameter size of each convolutional kernel is (3,8)), and a size of $7\times7$ kernel. We also define the second convolutional layer of the model `m2` to have four input channels, 64 output channels, and a size of $5\times5$ kernel.
m1 = Model(k1=3, k2=8) # Initializing the first model in the list. 
m2 = Model(7, 5)

